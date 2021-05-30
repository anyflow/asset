'use strict';

function runAsync(predicate, ...args) {
  (async () => await predicate(args))();
}

module.exports = {
  runAsync
};
