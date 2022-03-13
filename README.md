# Visual acuity charts

This repository contains a LaTeX file and a Python script for making
random [Snellen charts][snellen].  A PDF with 10 charts, meant to be
kept at a distance of 3 m, has been included with this repository.  To
generate the TeX commands for new charts, run `snellen.py`.  Then, edit
`snellen.tex` and change the distance `\factor` if required.  To compile
the file, run `make` or compile using XeLaTeX.

<img align="right" width=360px src="https://raw.githubusercontent.com/manu-mannattil/assets/master/vachart/snellen.svg"/>

## Background

The Snellen chart consists of a series of optotypes (usually the letters
C, D, E, F, L, O, P, T, and Z) in different sizes. Using elementary
trigonometry, the equation that relates the optotype width (or height)
<i>w</i>, the subtended angle φ, and the distance to the chart <i>d</i>,
is

<i>w</i> = 2<i>d</i> tan(φ/2)

A person's vision is considered normal (i.e., 6/6 or 20/20 vision) if he
or she can delineate 1-arcminute-wide features of an optotype that has
an angular width of 5 arcminutes.  Conventionally, the Snellen chart is
kept at a distance of 6 m.  This means that the optotype width must be

<i>w</i> = (12 m) × tan(π/4320) = 8.73 mm.

## Further reading

R. J. Kolker, [Subjective Refraction and Prescribing Glasses][sub] (American Academy of Opthalmology, San Francisco, CA, 2014).

A. R. Elkington, H. J. Frank, M. J. Greaney, Clinical Optics, 3rd ed. (Blackwell Science, Oxford, 1999).

## Disclaimer and license

This repository is for informational purposes only and do not constitute
medical advice. It is not intended to replace the advice of a qualified
health provider or a licensed optometrist.

[Optician Sans][optsans] is licensed under the [SIL Open Font
License][sil], Version 1.1.  All other material is in the public domain.
See the file UNLICENSE for more details.

[snellen]: https://en.wikipedia.org/wiki/Snellen_chart
[optsans]: https://optician-sans.com
[sil]: http://scripts.sil.org/OFL
[sub]: http://web.archive.org/web/20220309081507/https://www.aao.org/Assets/563fc40b-1466-477e-bc12-4e62f8b2d324/635476894936870000/subjective-refraction-prescribing-glasses-pdf
