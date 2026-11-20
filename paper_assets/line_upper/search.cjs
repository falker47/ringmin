// Seeded binary64 exploration. Exact certificates are constructed separately.
"use strict";
const fs = require("node:fs");
const path = require("node:path");

function randomGenerator(seed) {
  let state = seed >>> 0;
  return () => {
    state ^= state << 13;
    state ^= state >>> 17;
    state ^= state << 5;
    return (state >>> 0) / 4294967296;
  };
}

// The maximum uses every possible predecessor. Once x[j]+wi is
// below the incumbent, all earlier positions give a smaller candidate.
function suffix(order, weights, start, prefix, out) {
  for (let i = start; i < order.length; i++) {
    const wi = weights[order[i]];
    let best = 0;
    for (let j = i - 1; j >= 0; j--) {
      const xj = j < start ? prefix[j] : out[j];
      if (xj + wi < best) break;
      best = Math.max(best, xj + wi * weights[order[j]]);
    }
    out[i] = best;
  }
  return out[order.length - 1];
}

function alternating(n, shifted, slabs) {
  const m = n >> 1;
  const highRank = Array.from({ length: m }, (_, i) => i + 1);
  let start = 0;
  for (const numerator of slabs) {
    const length = 2 * Math.floor(numerator * m / 200000);
    for (let i = start + 2; i <= start + length; i += 2) {
      highRank[i - 1] = 2 * start + length + 2 - i;
    }
    start += length;
  }
  const word = [];
  for (let i = 0; i < m; i++) {
    word.push(i + 1, m + 1 + ((highRank[i] + shifted - 1) % m));
  }
  if (n % 2) word.push(n);
  return word;
}

function startingOrder(n, weights, attempt) {
  const m = n >> 1;
  const sweeps = [
    [0, []],
    [Math.floor(1093 * m / 10000), []],
    [Math.floor(1093 * m / 10000), [31903, 4370, 580, 5]],
  ];
  // Include both unshifted and reflected families; diversify the second run.
  if (attempt === 1) sweeps.push([Math.floor(0.08 * m), [27000, 6000]]);
  let best = Infinity;
  let selected;
  for (const [shift, slabs] of sweeps) {
    const template = alternating(n, shift, slabs);
    const offsets = new Set([0, 1, n-1, 2 * (m-shift) % n,
      ...Array.from({ length: 16 }, (_, i) => Math.floor(i * n / 16))]);
    for (const k of offsets) {
      const order = template.slice(k).concat(template.slice(0, k));
      const values = new Float64Array(n);
      const score = suffix(order, weights, 0, values, values);
      if (score < best) { best = score; selected = order; }
    }
  }
  return selected;
}


function backwards(order, weights, out) {
  for (let i = order.length - 1; i >= 0; i--) {
    let best = 0;
    const wi = weights[order[i]];
    for (let j = i + 1; j < order.length; j++) {
      if (out[j] + wi < best) break;
      best = Math.max(best, out[j] + wi * weights[order[j]]);
    }
    out[i] = best;
  }
}

// A path crosses the cut after b exactly once. The unchanged right suffix
// contributes its precomputed reverse distances; left distances change
// only from a onward. This makes a short-range proposal cheap to reject.
function bridge(order, weights, a, b, forward, reverse, scratch) {
  for (let i = a; i <= b; i++) {
    let best = 0;
    const wi = weights[order[i]];
    for (let j = i - 1; j >= 0; j--) {
      const x = j < a ? forward[j] : scratch[j];
      if (x + wi < best) break;
      best = Math.max(best, x + wi * weights[order[j]]);
    }
    scratch[i] = best;
  }
  if (b === order.length-1) return scratch[b];
  let best = scratch[b] + reverse[b+1];
  for (let i = b; i >= 0; i--) {
    const x = i < a ? forward[i] : scratch[i];
    if (x + 1 + reverse[b+1] < best) break;
    for (let j = b+1; j < order.length; j++) {
      if (x + 1 + reverse[j] < best) break;
      best = Math.max(best, x + weights[order[i]] * weights[order[j]] + reverse[j]);
    }
  }
  return best;
}

function polish(order, weights, history) {
  const n = order.length;
  const forward = new Float64Array(n), reverse = new Float64Array(n);
  const trial = new Float64Array(n);
  let span = suffix(order, weights, 0, forward, forward);
  backwards(order, weights, reverse);
  const gaps = [1,2,3,4,6,8,10,12,16,24,32];
  let used = history.at(-1)[0], index = 0;
  for (;;) {
    const old = span, target = 2*used;
    for (; used < target; used++, index++) {
      const i = index % n;
      const j = i + gaps[Math.floor(index / n) % gaps.length];
      if (j >= n) continue;
      [order[i],order[j]] = [order[j],order[i]];
      if (bridge(order, weights, i, j, forward, reverse, trial) < span-1e-10) {
        const value = suffix(order, weights, i, forward, trial);
        if (value < span-1e-10) {
          forward.set(trial.subarray(i), i);
          backwards(order, weights, reverse);
          span = value;
          continue;
        }
      }
      [order[i],order[j]] = [order[j],order[i]];
    }
    history.push([used, (span+1)/(Math.PI*n)]);
    if ((old-span)/(Math.PI*n) < 1e-6) return;
  }
}

function run(n, power, attempt, baseSeed, reference = false) {
  const seed = (baseSeed + 65537 * power + 101 * n + attempt) >>> 0;
  const rand = randomGenerator(seed);
  const weights = Float64Array.from({ length: n + 1 }, (_, k) =>
    power === 1 ? Math.sqrt(k / n) : k / n);
  const order = reference ? alternating(n, 0, []) : startingOrder(n, weights, attempt);
  const current = new Float64Array(n);
  const trial = new Float64Array(n);
  let span = suffix(order, weights, 0, current, current);
  let bestSpan = span, bestOrder = [...order];
  const history = [[0, (span + 1) / (Math.PI * n)]];
  let cumulative = 0;
  const limit = reference ? 12000 : (n < 20 ? 1024 : 262144);
  const initial = reference ? 12000 : (n < 20 ? 1024 : 4096);
  for (let target = initial; target <= limit; target *= 2) {
    const oldBest = bestSpan;
    for (; cumulative < target; cumulative++) {
      let i = Math.floor(rand() * n);
      const mode = rand();
      let j;
      if (mode < 0.45) {
        j = i + 2 * (1 + Math.floor(rand() * Math.min(12, n / 2)));
      } else if (mode < 0.80) {
        j = i + 2 * (1 + Math.floor(rand() * Math.max(1, n / 2 - 1)));
      } else {
        j = Math.floor(rand() * n);
      }
      j %= n;
      if (i === j) continue;
      if (i > j) [i,j] = [j,i];
      [order[i],order[j]] = [order[j],order[i]];
      const proposed = suffix(order, weights, i, current, trial);
      // Equal-span moves explore plateaus. Keep the best word independently.
      if (proposed <= span + 2e-13) {
        current.set(trial.subarray(i), i);
        span = proposed;
        if (span < bestSpan - 1e-13) { bestSpan = span; bestOrder = [...order]; }
      } else {
        [order[i],order[j]] = [order[j],order[i]];
      }
    }
    history.push([cumulative, (bestSpan + 1) / (Math.PI * n)]);
    if (history.length >= 3 && (oldBest - bestSpan) / (Math.PI * n) < 1e-6) break;
  }
  if (!reference && n >= 200 && history.at(-1)[0] === limit &&
      history.at(-2)[1] - history.at(-1)[1] >= 1e-6) {
    polish(bestOrder, weights, history);
  }
  return { seed, history, order: bestOrder };
}

const output = process.argv[2];
if (output === "--interleaved-reference") {
  for (const attempt of [0, 1]) {
    const r = run(400, 1, attempt, 20261119, true);
    console.log("INTERLEAVED_REFERENCE", r.seed, r.history.at(-1));
  }
  process.exit(0);
}
if (!output) throw Error("usage: node search.cjs OUTPUT_DIR [n ...]");
fs.mkdirSync(output, { recursive: true });
const sizes = process.argv.length > 3 ? process.argv.slice(3).map(Number)
  : [3, 4, 5, 6, 14, 200, 400, 800, 1600, 3200];
for (const n of sizes) {
  if (!Number.isSafeInteger(n) || n < 3) throw Error("invalid size");
  for (const power of [1, 2]) {
    const runs = [0,1].map(attempt => run(n, power, attempt, 20261119));
    const scores = runs.map(r => r.history.at(-1)[1]);
    const chosen = scores[0] <= scores[1] ? 0 : 1;
    const result = { n, power, order: runs[chosen].order, chosen,
      attempts: runs.map(r => ({ seed: r.seed, history: r.history })) };
    const name = "p" + power + "_n" + String(n).padStart(5, "0") + ".json";
    fs.writeFileSync(path.join(output, name), JSON.stringify(result) + "\n");
    console.log(name, scores[chosen], runs.map(r => r.history.at(-1)[0]).join("/"));
  }
}
