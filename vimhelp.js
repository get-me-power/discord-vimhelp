// You can search the help of Vim.
const {VimHelp} = require("vimhelp");
const argv = process.argv[2];
console.log("hoge");
console.log(process.argv[2]);

(async () => {
let vimHelp = new VimHelp();

let text = await vimHelp.search(argv);
console.log(text);
/* The following text is shown:
j               or                                      *j*
<Down>          or                                      *<Down>*
CTRL-J          or                                      *CTRL-J*
<NL>            or                                      *<NL>* *CTRL-N*
CTRL-N                  [count] lines downward |linewise|.
*/
})();
