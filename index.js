function decode(message_file) {
  var fs = require("fs");
  var OVERWRITE_DUPLICATE = true;
  var sentence = {};
  var steps = [];
  var message = fs.readFileSync(message_file, "utf8").split("\n");

  for (line in message) {
    var [n, word] = message[line].split(" ");
    n = parseInt(n);

    var nKey = (n * (n + 1)) / 2;
    var len = steps.length;
    var maxKey = (len * (len + 1)) / 2;

    // add more steps only when needed
    if (nKey > maxKey) {
      do {
        steps[len - 1] = maxKey;
        sentence[maxKey] = null;
        len = len + 1;
        maxKey = (len * (len + 1)) / 2;
      } while (nKey >= maxKey);
    }

    // add the word to the sentence object
    if (sentence[n] !== undefined) {
      if (OVERWRITE_DUPLICATE) {
        sentence[n] = word;
      } else if (sentence[n - 1] === null) {
        sentence[n] = word;
      }
    }
  }

  // compile the sentence object into a decoded string
  return steps
    .reduce((acc, val) => {
      return sentence[val] === null ? acc : acc + sentence[val] + " ";
    }, "")
    .slice(0, -1);
}

console.log(decode("example.txt"));
