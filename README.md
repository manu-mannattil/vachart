# Visual acuity charts

This repository contains a LaTeX file and a Python script for making
random [Snellen charts][snellen].  A [PDF][pdf] with 10 charts, meant to
be kept at a distance of 3 m, has been included with this repository.
To generate new charts, first edit `snellen.tex` and change the distance
`\factor` if required.  To compile the file, run `make` or compile using
XeLaTeX with the `--shell-escape` option.  When compiling the file, the
standard output of the `snellen.py` script, which produces LaTeX
commands to make random charts, is automatically included.  (This
assumes that your version of XeLaTeX comes with an `\input{|...}` that
allows capturing the standard outputs of commands.)

<img align="right" width=360px src="https://raw.githubusercontent.com/manu-mannattil/assets/master/vachart/snellen.svg"/>

## Background

The Snellen chart consists of a series of optotypes (usually the letters
C, D, E, F, L, O, P, T, and Z) in different sizes. Using elementary
trigonometry, the equation that relates the optotype width (or height)
$w$, the subtended angle $φ$, and the distance to the chart $d$,
is

$$w = 2d\tan(\varphi/2).$$

A person's vision is considered normal (i.e., 6/6 or 20/20 vision) if he
or she can delineate 1-arcminute-wide features of an optotype that has
an angular width of 5 arcminutes (= $π/2160~\text{rad}$).  So if the Snellen chart is to be kept
at a distance of 3m (as with the example PDF), the optotype width must
be

$$w = (2×3~\text{m})\times\tan[(\pi/2160)/2] = 4.36~\text{mm}.$$

## Further reading

R. J. Kolker, [Subjective Refraction and Prescribing Glasses][sub] (American Academy of Opthalmology, San Francisco, CA, 2014).

A. R. Elkington, H. J. Frank, M. J. Greaney, Clinical Optics, 3rd ed. (Blackwell Science, Oxford, 1999).

## Disclaimer and license

The contents of this repository are for informational purposes only and
do not constitute medical advice. They are not intended to replace the
advice of a licensed optometrist or a qualified health provider.

[Optician Sans][optsans] is licensed under the [SIL Open Font
License][sil], Version 1.1.  All other material is in the public domain.
See the file UNLICENSE for more details.

[snellen]: https://en.wikipedia.org/wiki/Snellen_chart
[optsans]: https://optician-sans.com
[sil]: http://scripts.sil.org/OFL
[sub]: http://web.archive.org/web/20220309081507/https://www.aao.org/Assets/563fc40b-1466-477e-bc12-4e62f8b2d324/635476894936870000/subjective-refraction-prescribing-glasses-pdf
[pdf]: https://raw.githubusercontent.com/manu-mannattil/vachart/master/snellen.pdf
