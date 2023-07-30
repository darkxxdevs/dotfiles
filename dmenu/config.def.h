//██████╗ ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
//██╔══██╗████╗ ████║██╔════╝████╗  ██║██║   ██║
//██║  ██║██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
//██║  ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
//██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
//╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
///////////////////////////////////////////////////?????/???????????????????????????????????????????????                                              

static int topbar = 1;                      /* -b  option; if 0, dmenu appears at bottom  */
/* -fn option overrides fonts[0]; default X11 font or font set */
static const char *fonts[] = {
	"JetBrains Mono:size=9:antialias=true:autohint:true",
	"Noto Color Emoji:size=8:antialias=true;autohint:true"
};
static const char *prompt      = NULL;      /* -p  option; prompt to the left of input field */
static const char *colors[SchemeLast][2] = {
	/*     fg         bg       */
	[SchemeNorm] = { "#ffffff", "#1e1e2e" },
	[SchemeSel] = { "#eeeeee", "#ce9df2" },
	[SchemeOut] = { "#ce9df2", "#1e1e2e" },
};
/* -l option; if nonzero, dmenu uses vertical list with given number of lines */
static unsigned int lines      = 5;

/*
 * Characters not considered part of a word while deleting words
 * for example: " /?\"&[]"
 */
static const char worddelimiters[] = " ";

