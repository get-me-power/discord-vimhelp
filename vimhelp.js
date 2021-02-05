const {VimHelp} = require("vimhelp");
const argv = process.argv[2];

(async () => {
let vimHelp = new VimHelp();

let text = await vimHelp.search(argv);
console.log(text);
})();
