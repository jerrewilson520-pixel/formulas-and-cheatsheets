# C151D07: data for CHEM151. Don't run this file.
D=(
"* x-axis = m/q (~ mass of a +1 ion); y-axis = relative abundance\n* "
"Highest-m/q major peak = molecular ion M^+ -> gives molar mass of "
"the molecule (usually)\n* Smaller peaks to the left = fragments; "
"a peak 1 unit to the right of M^+ = molecules with a heavier isotope"
" (e.g. C-13)\n* Atomic element X2 with two isotopes -> three molecul"
"ar peaks (light-light, light-heavy, heavy-heavy)",
"COMMON LOSSES FROM M^+\n* -1 (H)\n* -15 (CH3)\n* -17 (OH)\n* -18 "
"(H2O)\n* -29 (CHO or C2H5)\n* -31 (OCH3)\n* -35/-37 (Cl)\n* -79/-81 "
"(Br)\n\nISOTOPE PATTERNS\n* Chlorine: Cl-35 75.76%, Cl-37 24.24% "
"-> peaks 2 units apart in ~3:1 ratio\n* Bromine: Br-79 50.69%, Br-81"
" 49.31% -> peaks 2 units apart in ~1:1 ratio\n\nMETHOD: Identify "
"each peak\n1. Find M^+ and match it to the formula's molar mass "
"(use the most common isotopes: H-1, C-12, O-16, N-14, Cl-35, Br-79)."
"\n2. For each smaller peak, subtract from M^+ to find the lost piece"
"; write the ion's formula with a + charge.\n3. Peaks at M+1, M+2: "
"isotope versions of the same ion.\n4. For isotope pattern of X2: "
"P(light-light) = f_L^2, P(light-heavy) = 2 f_L f_H, P(heavy-heavy) "
"= f_H^2 (f = fractional abundance).",
"* m_C = m_CO2*(12.01/44.01)\n* m_H = m_H2O*(2*1.008/18.02)\n* m_O "
"= m_sample - m_C - m_H\n* %X = (subscript of X)*M_X/M_compound*100\n"
"* k = M(molecule)/M(empirical), with M(molecule) from the M^+ peak",
"* m_C, m_H, m_O = mass of each element in the original sample (g)\n*"
" m_CO2, m_H2O = masses of products collected (g)\n* m_sample = mass "
"of the original sample (g)\n* %X = mass percent of element X\n* "
"M_X = molar mass of element X\n* M_compound = molar mass of the "
"compound\n* k = multiplier: empirical -> molecular formula",
"METHOD: Empirical formula from mass percent (combustion analysis)\n1"
". Assume 100.0 g -> each % becomes grams.\n2. Grams of each element "
"/ that element's molar mass -> moles.\n3. Divide every mole value "
"by the smallest one.\n4. Not whole? Multiply all ratios by the same "
"factor: ~.5 -> x2, ~.33 or .67 -> x3, ~.25 or .75 -> x4, ~.2 -> "
"x5.\n5. Write the empirical formula (simplest whole-number ratio).\n"
"6. Molecular formula: k = M(molecule, from M^+ peak) / M(empirical);"
" multiply every subscript by k.\n\nMETHOD: From masses of CO2 and "
"H2O collected\n1. m_C = m_CO2 x 12.01/44.01\n2. m_H = m_H2O x 2(1.00"
"8)/18.02\n3. m_O = m_sample - m_C - m_H\n4. Then continue from step "
"2 above (grams -> moles -> ratios).",
)
