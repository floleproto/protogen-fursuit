
var args = process.argv
var exeq = require('exeq')

if (args.length != 3){ console.log("Argument manquant. (URL)"); return;}

console.log(args)

exeq("cd /var/lib/mpd/music", "youtube-dl -x --audio-format wav " + args[2]).then((log) => {
    console.log("Fin")
})
.catch((err) => console.error(err))