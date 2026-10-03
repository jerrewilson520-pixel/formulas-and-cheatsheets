# Chem 151 Formula Sheet -- Chemical Thinking Vol. I
# Source content for the TI-84 Evo app, written in plain ASCII so the
# calculator can display every character.
#
# Structure:  MODULES -> units -> four tabs
#   F = formulas            (list of str)
#   V = variables/constants (list of (symbol, meaning))
#   N = notes               (list of str)
#   C = cheats: methods, tables, shortcuts, traps (list of str)
#
# Text conventions (shown in the app's Notation Key):
#   x_1  subscript         x^2  superscript / power
#   *    multiply          /    divide
#   Delta = change (Greek capital delta), delta = partial charge
#   lambda, nu (frequency), nu~ (wavenumber), chi, mu, rho
#   <E_k> = average of E_k   SUM = sum of   ~ = approximately
#   -> gives / leads to   <-> both ways   # = triple bond (C#N)
#   Na^+, Cl^-, Ca^2+, SO4^2- = ion charges   degC = degrees C
#
# Multi-line strings: first line is a heading, following lines are
# bullets ("* ") or numbered steps ("1. ").


def U(title, F=(), V=(), N=(), C=()):
    return {"title": title, "F": list(F), "V": list(V), "N": list(N), "C": list(C)}


MODULES = []

# ---------------------------------------------------------------------
# 0. Constants and conversions
# ---------------------------------------------------------------------
MODULES.append({
    "title": "0 Constants+Conv",
    "full": "0. Constants and conversions",
    "units": [
        U("0.1 Constants",
          V=[
              ("N_A", "Avogadro's number = 6.022x10^23 particles/mol. Use for moles <-> particles"),
              ("k_B", "Boltzmann constant = 1.380x10^-23 J/K. Use for ideal gas per particle"),
              ("R", "gas constant (energy) = 8.314 J/(K*mol). Use for energy problems"),
              ("R", "gas constant (gas law) = 0.08206 L*atm/(K*mol). Use for PV = nRT with L and atm"),
              ("R", "gas constant (cal) = 1.986 cal/(K*mol). Use for calorie problems"),
              ("h", "Planck's constant = 6.626x10^-34 J*s. Use for photon energy"),
              ("c", "speed of light (vacuum) = 3.00x10^8 m/s. Use for wavelength <-> frequency"),
              ("e", "electron / proton charge = +/-1.602x10^-19 C. Use for Coulomb problems"),
              ("V_m", "molar volume of ideal gas at STP = 22.41 L/mol (STP = 273.15 K, 1 atm)"),
          ],
          N=[
              "Every calculation in this book starts by converting to these units.",
              "Always convert T to kelvin and V to liters before using R.",
          ]),
        U("0.2 Conversions",
          F=[
              "T(K) = T(degC) + 273.15",
              "Pressure: 1 atm = 101,325 Pa = 760 mm Hg = 760 torr",
              "1 Pa = 1 N/m^2",
              "Energy: 1 cal = 4.184 J; 1 kJ = 1000 J",
              "Volume: 1 L = 1000 mL = 1000 cm^3; 1 m^3 = 1000 L",
              "Mass: 1 g = 1000 mg; 1 mg = 1000 ug; 1 kg = 1000 g",
              "mole fraction = ppmv x 10^-6",
          ],
          V=[
              ("T(K)", "temperature in kelvin"),
              ("T(degC)", "temperature in degrees Celsius"),
              ("ppmv", "moles of X per 10^6 moles of air"),
              ("ug", "microgram (u = micro = 10^-6)"),
          ],
          C=[
              "PREFIXES\n"
              "* G = 10^9\n"
              "* M = 10^6\n"
              "* k = 10^3\n"
              "* h = 10^2\n"
              "* c = 10^-2\n"
              "* m = 10^-3\n"
              "* u (micro, mu) = 10^-6\n"
              "* n = 10^-9\n"
              "* p = 10^-12\n"
              "* f = 10^-15",
          ]),
        U("0.3 Factor-label",
          C=[
              "METHOD: Factor-label method (works for every unit problem)\n"
              "1. Write what you have with its units and what you want.\n"
              "2. Multiply by conversion factors arranged so the old unit cancels (old unit on the bottom).\n"
              "3. Check the units left over match what you want, then compute.",
          ]),
    ],
})

# ---------------------------------------------------------------------
# 1. Unit 1 (M1-M2): Phases, separations, particulate model
# ---------------------------------------------------------------------
MODULES.append({
    "title": "1 U1(M1-2) Phases",
    "full": "1. Unit 1 (M1-M2): Phases, separations, particulate model",
    "units": [
        U("1.1 Differentiating",
          N=[
              "INTENSIVE (doesn't depend on amount): melting point, boiling point, density, conductivity, solubility -> good for identifying a substance",
              "EXTENSIVE (depends on amount): mass, volume -> useless for identifying",
              "T and P are intensive but describe the whole system, not one component -> not differentiating characteristics",
              "Good characteristic = unique value per substance + independent of sample size + measurable selectively",
          ]),
        U("1.2 Heat/cool curves",
          N=[
              "Graphs: heating / cooling curves (T vs t) and DeltaE vs T",
              "Sloped segment = one phase heating/cooling (T changes)",
              "Flat segment = phase change; T stays constant until one phase is fully converted",
              "Melting, boiling, sublimation absorb energy (DeltaE > 0); freezing, condensing, deposition release energy (DeltaE < 0)",
              "Boiling plateau is longer than melting plateau (bigger density change -> more energy)",
              "On a DeltaE vs T plot, phase changes are VERTICAL JUMPS at T_m and T_b",
          ],
          V=[
              ("T_m", "melting point temperature"),
              ("T_b", "boiling point temperature"),
              ("DeltaE", "energy change (> 0 absorbed, < 0 released)"),
          ],
          C=[
              "HOW TO SKETCH A HEATING CURVE\n"
              "1. Mark T_m and T_b on the T-axis.\n"
              "2. Draw slopes for each phase.\n"
              "3. Draw flat lines at T_m and T_b.\n"
              "4. Make the T_b plateau longer.",
          ]),
        U("1.3 Phase diagrams",
          N=[
              "Phase diagram = P vs T",
              "REGION = only stable phase; LINE = two phases coexist; TRIPLE POINT = all three coexist; CRITICAL POINT = end of liquid-gas line, beyond it -> supercritical fluid",
              "Liquid-gas line = vapor pressure curve",
              "Normal boiling/melting point = where that line crosses P = 1 atm",
              "Water: solid-liquid line tilts LEFT (ice less dense than liquid) -> raising P can melt ice; triple point 0.01 degC, 0.006 atm (4.58 mm Hg); critical point 374 degC, 218 atm",
              "CO2: triple point -57 degC, 5.2 atm -> at 1 atm it SUBLIMES at -78 degC (never liquid at 1 atm); critical point 31 degC, 73 atm",
          ],
          C=[
              "METHOD: \"What phase is X at T, P? What changes if...?\"\n"
              "1. Convert T and P to the diagram's units (watch for log-scale P axes).\n"
              "2. Plot the point; the region it lands in = stable phase.\n"
              "3. Changing T at constant P -> move horizontally; each line crossed = a phase change at that T.\n"
              "4. Changing P at constant T -> move vertically; each line crossed = a phase change at that P.\n"
              "5. Name each transition (melting, boiling, sublimation, etc.) and read the T or P where you cross.",
          ]),
        U("1.4 Vapor pressure",
          N=[
              "Boiling happens when vapor pressure = external pressure",
              "Higher vapor pressure at a given T = more volatile = weaker attractions between particles = lower boiling point",
              "Lower external P (high altitude, e.g. Tucson ~ 700 mm Hg) -> lower boiling point",
          ],
          C=[
              "METHOD: Boiling point at a given pressure from a VP graph\n"
              "1. Draw a horizontal line at the external pressure.\n"
              "2. Where it hits each curve, drop down to the T-axis -> that substance's boiling point.\n"
              "3. The curve that hits first (leftmost) boils first = most volatile.",
          ]),
        U("1.5 Separations",
          C=[
              "SEPARATION TECHNIQUES (technique: differentiating property -> what separates)\n"
              "* Filtration: phase (solid vs fluid) -> solid from liquid/gas\n"
              "* Crystallization: solubility (changes with T or concentration) -> a pure solid out of a solution\n"
              "* Distillation: boiling point -> liquids; most volatile comes out first\n"
              "* Fractional distillation: boiling point (close values) -> column hot at bottom, cool at top; most volatile condenses highest\n"
              "* Chromatography: strength of attraction to the stationary phase -> weakly attracted substances exit first (shorter retention time)",
              "METHOD: Design a separation (e.g. a mixture of gases or liquids)\n"
              "1. List each component's T_m and T_b (or VP curve).\n"
              "2. Pick the property that differs most -> that's the differentiating characteristic.\n"
              "3. Order components by boiling point; when cooling a gas mixture, the highest T_b condenses first; when heating a liquid, the lowest T_b boils off first.\n"
              "4. Give the temperature for each step, set between consecutive boiling points.\n"
              "5. State the outcome of each step (what's collected, what remains).",
              "METHOD: Fractional distillation column (trays)\n"
              "1. Sort all substances by T_b.\n"
              "2. For each fraction you want, find the T_b range it needs (e.g. \"liquid between 5 degC and 38 degC\" -> needs T_m < 5 degC and T_b > 38 degC).\n"
              "3. Place a tray at a temperature between the last substance of one fraction and the first substance of the next.\n"
              "4. Number of trays = number of boundaries between fractions inside the column; top exhaust = gases more volatile than the top T; bottom = everything above the bottom T.\n"
              "5. List which substances end up in each fraction.",
          ]),
        U("1.6 Particulate model",
          F=[
              "<E_k> = (1/2)*m*<v>^2",
          ],
          V=[
              ("<E_k>", "average kinetic energy per particle (J)"),
              ("m", "mass of one particle (kg)"),
              ("<v>", "average particle speed (m/s)"),
          ],
          N=[
              "PARTICULATE MODEL OF MATTER\n"
              "1. Matter is made of tiny (~1 nm) identical particles.\n"
              "2. Particles move constantly and randomly through empty space.\n"
              "3. Particles attract at long range and repel at short range.",
              "T IS A MEASURE OF <E_k>. Same T -> same <E_k>, regardless of substance or phase",
              "At the same T: lighter particles move faster (m down -> v up)",
              "At a triple point all three phases have the SAME average speed (same T)",
              "Higher T -> speed distribution shifts right and flattens (more fast particles)",
          ]),
        U("1.7 Ideal gases",
          F=[
              "P = k_B*N*T/V",
              "N = P*V/(k_B*T)",
              "P prop. to T (const N, V)",
              "P prop. to N (const T, V)",
              "P prop. to 1/V (const N, T)",
              "Gas changes conditions (N fixed): P_1*V_1/T_1 = P_2*V_2/T_2",
              "V_2 = V_1*(P_1/P_2)*(T_2/T_1)",
          ],
          V=[
              ("P", "pressure (Pa)"),
              ("N", "number of particles"),
              ("T", "absolute temperature (K)"),
              ("V", "volume (m^3)"),
              ("k_B", "Boltzmann constant = 1.380x10^-23 J/K"),
              ("X_1, X_2", "subscript 1 = initial state, 2 = final state; T in K; P and V in any matching units"),
          ],
          N=[
              "Same T, P, V -> same N for any gas (Avogadro's hypothesis); P does NOT depend on particle mass",
              "Ideal behavior: high T, low P (particles far apart, interactions negligible)",
              "REAL GASES: repulsion (particle size) -> less free volume -> P HIGHER than ideal; attraction -> particles hit walls less -> P LOWER than ideal. Deviations grow near condensation (low T, high P).",
          ],
          C=[
              "METHOD: Gas changes conditions (balloon/lungs rising or diving) -- since N is fixed, P_1*V_1/T_1 = P_2*V_2/T_2\n"
              "1. List P_1, V_1, T_1, P_2, T_2 (convert T to K).\n"
              "2. Solve V_2 = V_1*(P_1/P_2)*(T_2/T_1).\n"
              "3. Sanity check: lower P -> bigger V; lower T -> smaller V.",
          ]),
        U("1.8 Potential energy",
          V=[
              ("E_p", "potential energy (0 when particles are infinitely far apart)"),
              ("E_k", "kinetic energy"),
          ],
          N=[
              "E_p = 0 when particles are infinitely far apart",
              "Attraction: E_p becomes more negative as particles get closer, and E_k increases",
              "Repulsion: E_p increases as particles get closer, and E_k decreases",
              "During a phase change at constant T, added energy goes into E_p (separating particles), not E_k -> that's why T stays flat",
              "Condensing/freezing: E_p drops, extra E_k is passed to surroundings as heat released (latent heat)",
              "Stronger attractions -> more energy to separate -> higher T_m and T_b",
          ]),
        U("1.9 PEC diagrams",
          V=[
              ("PEC", "potential energy-configuration diagram"),
              ("y-axis", "E_p"),
              ("x-axis", "number of configurations"),
          ],
          N=[
              "PEC = potential energy-configuration diagram",
              "y-axis = E_p; x-axis = number of configurations",
              "Systems favor LOW E_p and MANY configurations",
          ],
          C=[
              "WHAT EACH CONDITION FAVORS\n"
              "* Low T: lower E_p state (e.g. liquid, solid)\n"
              "* High T: more-configurations state (e.g. gas)\n"
              "* High P: fewer configurations (denser state)\n"
              "* Low P: more configurations (gas)",
              "METHOD: Written PEC justification\n"
              "1. Place each state: lower E_p = stronger attractions (liquid/solid); more configurations = more space to occupy (gas).\n"
              "2. State which factor wins under the stated condition (T or P).\n"
              "3. Use the template: \"State A has lower E_p because particles are closer and attract more strongly. State B has more configurations because particles can occupy more space. At [low/high T], [E_p / configurations] dominates, so [state] is favored.\"\n"
              "4. Comparing two substances: the liquid placed LOWER on E_p has stronger attractions -> higher boiling point.",
          ]),
        U("1.10 Emergent/traps",
          N=[
              "Emergent properties (only exist for many particles): T_m, T_b, density, viscosity, color, hardness, malleability, conductivity",
          ],
          C=[
              "COMMON TRAPS\n"
              "* Individual particles do NOT melt, expand, soften, get heavier, or change size during heating or phase changes; only their spacing and energy change\n"
              "* Ice floats because particles in ice are farther apart, not lighter or smaller\n"
              "* Particles in solids still move (vibrate); they can't move past one another\n"
              "* Bubbles in boiling water are water particles, not H2 and O2",
          ]),
    ],
})

# ---------------------------------------------------------------------
# 2. Unit 1 (M3-M4): Counting particles, gases, composition
# ---------------------------------------------------------------------
MODULES.append({
    "title": "2 U1(M3-4) Counting",
    "full": "2. Unit 1 (M3-M4): Counting particles, gases, composition",
    "units": [
        U("2.1 Classifying matter",
          N=[
              "Elementary substance: one type of atom (Ar, O2, P4); can't be decomposed",
              "Compound: 2+ types of atoms bonded; decomposes into elements in a fixed ratio",
              "Mixture: 2+ different kinds of particles not bonded to each other",
              "Molecular elements: H2, N2, O2, F2, Cl2, Br2, I2, P4, S8 (use the molecule's mass, e.g. M(O2) = 32.00)",
              "Molecular compound: nonmetal + nonmetal, discrete molecules, poor conductors",
              "Ionic compound: metal + nonmetal, network of cations (+) and anions (-), high T_m, conduct when molten or dissolved; formula unit = lowest ion ratio",
          ],
          C=[
              "NAMING BINARY COMPOUNDS\n"
              "* Ionic: cation name + anion root + \"-ide\" (NaCl sodium chloride, Al2O3 aluminum oxide); no prefixes; Roman numeral for metals with several charges (Cu^2+ = copper(II))\n"
              "* Molecular: element farther left (or lower if same group) first; second gets \"-ide\"; prefixes mono, di, tri, tetra, penta, hexa; no \"mono\" on the first element (CO carbon monoxide, N2O dinitrogen monoxide, PCl3 phosphorus trichloride)",
          ]),
        U("2.2 Mass/mol/particles",
          F=[
              "n = m/M",
              "N = n*N_A",
              "m = n*M",
              "n = N/N_A",
              "M(compound) = SUM(subscript*M_atom)",
              "Mass of one particle = M/N_A (g/particle)",
              "Liquid by volume: m = V*d",
          ],
          V=[
              ("n", "amount of substance (mol)"),
              ("m", "mass of sample (g)"),
              ("M", "molar mass (g/mol)"),
              ("N", "number of particles"),
              ("N_A", "Avogadro's number = 6.022x10^23 /mol"),
              ("d", "density (g/mL)"),
              ("M_atom", "molar mass of one atom (g/mol)"),
          ],
          N=[
              "Same mass number of grams as atomic mass -> same number of atoms (4.003 g He and 39.95 g Ar both = 1 mol)",
          ],
          C=[
              "EXAMPLE PATTERN\n"
              "* M(CO2) = 12.01 + 2(16.00) = 44.01 g/mol",
              "METHOD: Any \"how many particles / grams / moles\" problem\n"
              "1. Find the molar mass from the formula (count every atom).\n"
              "2. Grams -> moles: divide by M. Moles -> particles: multiply by N_A.\n"
              "3. If asked for atoms of one element: particles x (subscript of that element).\n"
              "4. Liquid given by volume: first m = V x d (d = density, g/mL).",
          ]),
        U("2.3 Solutions",
          F=[
              "[A] = n_A/V_solution",
              "mass % = (mass of solute/mass of solution)*100",
              "n = [A]*V",
              "m = n*M",
          ],
          V=[
              ("[A]", "molarity of solute A (mol/L = M)"),
              ("n_A", "moles of solute"),
              ("V_solution", "volume of solution (L)"),
          ],
          C=[
              "METHOD: Molarity problems\n"
              "1. Grams of solute -> moles (divide by M).\n"
              "2. Volume -> liters.\n"
              "3. [A] = n/V. To go backwards: n = [A] x V, then m = n x M.\n"
              "4. Mass % to molarity: assume 100 g solution (or 1 L using density) -> grams solute -> moles -> divide by liters of solution.",
          ]),
        U("2.4 Ideal gas (molar)",
          F=[
              "PV = nRT = (m/M)*R*T",
              "M = m*R*T/(P*V)",
              "d = P*M/(R*T)",
              "n/V = P/(R*T)",
              "Other Unit 1 ratio problems: Percent increase = (new-old)/old*100",
              "Molecules of B per molecule of A = (m_B/M_B)/(m_A/M_A)",
              "GWP per molecule = (GWP per gram)*M(gas)/M(CO2)",
          ],
          V=[
              ("P", "pressure (atm)"),
              ("V", "volume (L)"),
              ("n", "moles of gas"),
              ("R", "0.08206 L*atm/(K*mol)"),
              ("T", "temperature (K)"),
              ("m", "mass of gas (g)"),
              ("M", "molar mass (g/mol)"),
              ("d", "gas density (g/L)"),
              ("n/V", "molar concentration of gas (mol/L)"),
              ("GWP", "global warming potential; GWP per molecule = how many CO2 molecules equal one molecule of the gas"),
          ],
          N=[
              "1 mol of ideal gas at STP (0 degC, 1 atm) = 22.41 L; at 25 degC, 1 atm = 24.47 L",
              "Volume % of a gas in a mixture = mole % (e.g. air is 78.08% N2 by volume -> 0.7808 of the moles)",
          ],
          C=[
              "METHOD: Identify an unknown gas\n"
              "1. Convert m to g, V to L, P to atm, T to K.\n"
              "2. M = mRT / PV.\n"
              "3. Match M to a formula (e.g. 28 g/mol from C and O -> CO).",
              "METHOD: Convert pollutant concentrations (mg/m^3 <-> mol/L <-> molecules/mL <-> ppmv)\n"
              "1. mg/m^3 -> g/L: x (1 g / 1000 mg) x (1 m^3 / 1000 L) -> overall divide by 10^6.\n"
              "2. g/L -> mol/L: divide by M.\n"
              "3. mol/L -> molecules/mL: x N_A, then divide by 1000.\n"
              "4. To ppmv: moles of air per L = P / RT; mole fraction = (mol pollutant/L) / (mol air/L); ppmv = mole fraction x 10^6.\n"
              "5. Changing T at fixed mole fraction: gas concentration in mol/L scales by T_1/T_2 (colder -> more concentrated).",
          ]),
        U("2.5 Subatomic model",
          F=[
              "A = Z + N_n",
              "charge = Z - (#e^-)",
          ],
          V=[
              ("A", "mass number (protons + neutrons)"),
              ("Z", "atomic number = number of protons (defines the element)"),
              ("N_n", "number of neutrons"),
              ("#e^-", "number of electrons"),
          ],
          N=[
              "Isotopes: same Z, different neutrons (written with A as superscript and Z as subscript, e.g. B-10 and B-11)",
              "Ions: neutral atom loses e^- -> cation (+), gains e^- -> anion (-); Z never changes",
              "Nucleus radius ~ 10^-14 m vs atom ~ 10^-10 m; mostly empty space (Rutherford's gold foil)",
              "amu scale set by carbon-12 = exactly 12 amu",
          ],
          C=[
              "SUBATOMIC PARTICLES (charge; mass; location)\n"
              "* Proton p^+: +1 (1.602x10^-19 C); 1.673x10^-27 kg; nucleus\n"
              "* Neutron n^0: 0; 1.675x10^-27 kg; nucleus\n"
              "* Electron e^-: -1; 9.109x10^-31 kg; around nucleus",
          ]),
        U("2.6 Avg atomic mass",
          F=[
              "r.a.m. = SUM(isotope mass * %abundance)/100",
              "Two isotopes, only average known: x*m_1 + (1-x)*m_2 = average; solve for x",
          ],
          V=[
              ("r.a.m.", "average relative atomic mass (amu = g/mol)"),
              ("% abundance", "percent of atoms that are that isotope"),
              ("x", "fractional abundance of isotope 1 (1 - x for isotope 2)"),
              ("m_1, m_2", "masses of the two isotopes"),
          ],
          C=[
              "METHOD: Average atomic mass from isotopes\n"
              "1. Read each isotope's mass (m/q) and % abundance from the spectrum.\n"
              "2. Multiply each mass by its %; add; divide by 100.\n"
              "3. Two isotopes and only the average known: x(m_1) + (1 - x)(m_2) = average, solve for x.\n"
              "4. Check: the answer should sit closer to the more abundant isotope.",
          ]),
        U("2.7 Mass spectra",
          F=[
              "Isotope pattern of X2: P(light-light) = f_L^2",
              "P(light-heavy) = 2*f_L*f_H",
              "P(heavy-heavy) = f_H^2",
          ],
          V=[
              ("m/q", "x-axis: mass-to-charge (~ mass of a +1 ion)"),
              ("M^+", "molecular ion (highest-m/q major peak)"),
              ("f", "fractional abundance"),
              ("f_L, f_H", "fractional abundance of light / heavy isotope"),
          ],
          N=[
              "x-axis = m/q (~ mass of a +1 ion); y-axis = relative abundance",
              "Highest-m/q major peak = molecular ion M^+ -> gives molar mass of the molecule (usually)",
              "Smaller peaks to the left = fragments; a peak 1 unit to the right of M^+ = molecules with a heavier isotope (e.g. C-13)",
              "Atomic element X2 with two isotopes -> three molecular peaks (light-light, light-heavy, heavy-heavy)",
          ],
          C=[
              "COMMON LOSSES FROM M^+\n"
              "* -1 (H)\n"
              "* -15 (CH3)\n"
              "* -17 (OH)\n"
              "* -18 (H2O)\n"
              "* -29 (CHO or C2H5)\n"
              "* -31 (OCH3)\n"
              "* -35/-37 (Cl)\n"
              "* -79/-81 (Br)",
              "ISOTOPE PATTERNS\n"
              "* Chlorine: Cl-35 75.76%, Cl-37 24.24% -> peaks 2 units apart in ~3:1 ratio\n"
              "* Bromine: Br-79 50.69%, Br-81 49.31% -> peaks 2 units apart in ~1:1 ratio",
              "METHOD: Identify each peak\n"
              "1. Find M^+ and match it to the formula's molar mass (use the most common isotopes: H-1, C-12, O-16, N-14, Cl-35, Br-79).\n"
              "2. For each smaller peak, subtract from M^+ to find the lost piece; write the ion's formula with a + charge.\n"
              "3. Peaks at M+1, M+2: isotope versions of the same ion.\n"
              "4. For isotope pattern of X2: P(light-light) = f_L^2, P(light-heavy) = 2 f_L f_H, P(heavy-heavy) = f_H^2 (f = fractional abundance).",
          ]),
        U("2.8 Empirical formulas",
          F=[
              "m_C = m_CO2*(12.01/44.01)",
              "m_H = m_H2O*(2*1.008/18.02)",
              "m_O = m_sample - m_C - m_H",
              "%X = (subscript of X)*M_X/M_compound*100",
              "k = M(molecule)/M(empirical), with M(molecule) from the M^+ peak",
          ],
          V=[
              ("m_C, m_H, m_O", "mass of each element in the original sample (g)"),
              ("m_CO2, m_H2O", "masses of products collected (g)"),
              ("m_sample", "mass of the original sample (g)"),
              ("%X", "mass percent of element X"),
              ("M_X", "molar mass of element X"),
              ("M_compound", "molar mass of the compound"),
              ("k", "multiplier: empirical -> molecular formula"),
          ],
          C=[
              "METHOD: Empirical formula from mass percent (combustion analysis)\n"
              "1. Assume 100.0 g -> each % becomes grams.\n"
              "2. Grams of each element / that element's molar mass -> moles.\n"
              "3. Divide every mole value by the smallest one.\n"
              "4. Not whole? Multiply all ratios by the same factor: ~.5 -> x2, ~.33 or .67 -> x3, ~.25 or .75 -> x4, ~.2 -> x5.\n"
              "5. Write the empirical formula (simplest whole-number ratio).\n"
              "6. Molecular formula: k = M(molecule, from M^+ peak) / M(empirical); multiply every subscript by k.",
              "METHOD: From masses of CO2 and H2O collected\n"
              "1. m_C = m_CO2 x 12.01/44.01\n"
              "2. m_H = m_H2O x 2(1.008)/18.02\n"
              "3. m_O = m_sample - m_C - m_H\n"
              "4. Then continue from step 2 above (grams -> moles -> ratios).",
          ]),
    ],
})

# ---------------------------------------------------------------------
# 3. Unit 2: Light, atomic structure, Lewis structures, geometry, polarity
# ---------------------------------------------------------------------
MODULES.append({
    "title": "3 U2 Light/Atom/Bond",
    "full": "3. Unit 2: Light, atomic structure, Lewis structures, geometry, polarity",
    "units": [
        U("3.1 EM radiation",
          F=[
              "lambda*nu = c",
              "E = h*nu = h*c/lambda",
              "nu~ = 1/lambda",
              "E = h*c*nu~",
              "Per mole of photons: E_molar = N_A*h*nu (J/mol); divide by 1000 for kJ/mol",
              "Shortcut: E(kJ/mol) ~ 1.197x10^5/lambda(nm)",
              "Shortcut: E(kJ/mol) ~ 0.01197*nu~(cm^-1)",
          ],
          V=[
              ("lambda", "wavelength (m)"),
              ("nu", "frequency (s^-1 = Hz)"),
              ("c", "speed of light = 3.00x10^8 m/s (3.00x10^10 cm/s for wavenumbers, lambda in cm)"),
              ("E", "energy of ONE photon (J)"),
              ("h", "Planck's constant = 6.626x10^-34 J*s"),
              ("nu~", "wavenumber (cm^-1, IR spectra)"),
              ("E_molar", "energy per mole of photons (J/mol)"),
          ],
          N=[
              "For wavenumbers use c = 3.00x10^10 cm/s (lambda in cm)",
              "Longer lambda <-> lower nu <-> lower E",
          ],
          C=[
              "METHOD: lambda <-> nu <-> E (per photon and per mole)\n"
              "1. Convert lambda to meters (nm x 10^-9) or nu~ to m^-1 (cm^-1 x 100).\n"
              "2. nu = c/lambda; E = h*nu (J per photon).\n"
              "3. x N_A, divide by 1000 -> kJ/mol.\n"
              "4. Backwards (given DeltaE): per photon E = DeltaE(J/mol)/N_A; lambda = hc/E; name the region.",
              "EM REGIONS, long lambda -> short lambda (approx lambda; energy kJ/mol; what it does)\n"
              "* Radio / microwave: m to mm; 10^-3 to 10^-1; rotational transitions\n"
              "* Infrared (IR): ~1 mm to 700 nm; 10^-1 to 10^2; vibrational transitions (stretch, bend)\n"
              "* Visible: 700 nm (red) to 400 nm (violet); ~170 to 300; electron excitation\n"
              "* Ultraviolet (UV): 400 to 10 nm; 10^2 to 10^3; electron excitation, bond breaking, ionization\n"
              "* X-ray / gamma: < 10 nm; > 10^4; removes core electrons",
          ]),
        U("3.2 Quantization/PES",
          F=[
              "|DeltaE| = E_upper - E_lower = h*nu",
              "E_I = h*nu - E_k",
          ],
          V=[
              ("DeltaE", "energy gap between two levels (J per photon)"),
              ("E_upper, E_lower", "energies of the upper and lower levels"),
              ("E_I", "ionization energy (energy to remove an electron)"),
              ("E_k", "kinetic energy of the ejected electron"),
          ],
          N=[
              "Energy transfer only in whole photons; atoms/molecules only exist in discrete energy levels",
              "Absorption and emission lines of an element appear at the SAME lambda; each line = one transition",
              "Photoelectric effect: ejection only if h*nu > threshold; KE of electron grows with nu, not with intensity (intensity = number of photons)",
              "Ground state = lowest levels filled; excited state = electron promoted",
              "Electron as a wave: smaller space -> shorter wavelength -> higher kinetic energy; delocalization (spreading out, e.g. bonding) lowers kinetic energy",
              "Blackbody: hotter object -> peak shifts to shorter lambda (red -> white -> blue) and more total energy",
              "Molecular bands are broad because neighboring molecules shift energy levels slightly",
          ]),
        U("3.3 e- config/trends",
          V=[
              ("n", "shell number"),
              ("Z", "atomic number (= number of e^- in a neutral atom)"),
              ("chi", "electronegativity"),
          ],
          N=[
              "Each orbital holds 2 e^- with opposite spins (Pauli); e^- occupy empty orbitals singly before pairing",
              "Noble gas notation: [previous noble gas] + outer electrons (Ge = [Ar] 4s^2 3d^10 4p^2)",
              "Valence electrons = outermost s + p electrons (group 1-2: group number; group 13-18: group number - 10)",
              "Big jump in radius and drop in ionization energy when a new shell starts (He -> Li, Ne -> Na)",
          ],
          C=[
              "SHELLS (shell n: subshells; max e^- in subshell; orbitals in subshell)\n"
              "* n=1: s; 2; 1\n"
              "* n=2: s, p; 2, 6; 1, 3\n"
              "* n=3: s, p, d; 2, 6, 10; 1, 3, 5\n"
              "* n=4: s, p, d, f; 2, 6, 10, 14; 1, 3, 5, 7",
              "FILLING ORDER\n"
              "* 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p",
              "METHOD: Write a configuration\n"
              "1. Find Z (= number of e^- for a neutral atom; subtract for cations, add for anions).\n"
              "2. Fill in order until all e^- are placed, or start from the previous noble gas.\n"
              "3. Check: superscripts add to the electron count.",
              "METHOD: Read/sketch a PES spectrum\n"
              "* Each peak = one subshell; peak height prop. to number of e^- in it (2, 6, 10...); peaks at higher ionization energy = closer to the nucleus (1s is the highest)\n"
              "* Number of peaks and heights -> configuration -> identify the element",
              "PERIODIC TRENDS (across a period L->R; down a group; why)\n"
              "* Atomic radius: decreases; increases; more protons pull same shell in; new shell farther out\n"
              "* First ionization energy: increases; decreases; e^- held tighter when closer and more nuclear charge\n"
              "* Electronegativity chi: increases; decreases; same as ionization energy",
          ]),
        U("3.4 Valence",
          F=[
              "bonds = (max valence-shell occupancy) - (# valence e^-)",
          ],
          V=[
              ("max occupancy", "2 for H, 8 for other nonmetals"),
              ("# valence e^-", "number of valence electrons"),
              ("bonds", "number of bonds the atom usually forms (bonding capacity)"),
          ],
          N=[
              "Typical bonds: H 1, C 4, N 3, O 2, halogens (F, Cl, Br, I) 1, noble gases 0",
              "Larger atoms can exceed the octet: P can form 5, S can form 6 (SF6, H2SO4)",
              "Odd total e^- count -> radical (unpaired electron, very reactive: .OH, NO, NO2)",
          ]),
        U("3.5 Lewis structures",
          N=[
              "RESONANCE: more than one valid placement of a double bond (O3, CO3^2-, NO3^-, SO2). Real molecule is an average: identical bonds of intermediate length. Draw all forms with <->. More resonance forms -> more stable",
              "Bond length: triple < double < single; bond strength: triple > double > single",
          ],
          C=[
              "METHOD: Draw a Lewis structure\n"
              "1. Pick the central atom: highest valence (most bonds); if tied, the larger atom. H and F are never central.\n"
              "2. Count total valence e^- (sum over atoms). Anion: add e^- equal to the charge. Cation: subtract.\n"
              "3. Connect central atom to each outer atom with single bonds (2 e^- each).\n"
              "4. Put remaining e^- as lone pairs on outer atoms first (to 8; H gets 2), then any leftovers on the central atom.\n"
              "5. Central atom short of 8? Move lone pairs from outer atoms into double or triple bonds.\n"
              "6. Check: total e^- used = count from step 2; each atom has its usual number of bonds. Ions go in brackets with the charge outside.",
              "COMMON PATTERNS\n"
              "* C = four single, or two single + one double, or one single + one triple, or two double\n"
              "* O = two single or one double, plus 2 lone pairs\n"
              "* N = three single (one double + one single, or one triple), plus 1 lone pair",
          ]),
        U("3.6 IR spectroscopy",
          V=[
              ("nu~", "wavenumber (cm^-1)"),
          ],
          N=[
              "IR spectroscopy tells connectivity (which bonds exist)",
              "Stronger bonds and lighter atoms -> higher wavenumber",
              "A vibration absorbs IR only if it changes the molecule's dipole moment (IR active) -> greenhouse gases (CO2, H2O, CH4, N2O, O3); N2, O2 are not",
          ],
          C=[
              "IR TABLE (wavenumber cm^-1: bond / vibration)\n"
              "* ~3200-3600 (broad): O-H, N-H stretch\n"
              "* ~2800-3100: C-H stretch\n"
              "* ~2100-2300: triple bonds C#C, C#N\n"
              "* ~1600-1800: double bonds; C=O strong near 1700\n"
              "* ~1350-1500: C-H bends (CH2, CH3)\n"
              "* ~1000-1300: single bonds C-O, C-N, C-C",
              "METHOD: Structure from combustion + MS + IR\n"
              "1. % composition -> empirical formula (Section 2.8).\n"
              "2. M^+ peak -> molecular formula.\n"
              "3. IR bands -> which bonds exist (O-H? C=O? C#N?).\n"
              "4. Draw Lewis structures with the right bonds and valences; check MS fragments match pieces (e.g. M - 15 = lost CH3, M - 17 = lost OH).",
          ]),
        U("3.7 VSEPR geometry",
          N=[
              "Electron domain = a region of e^- density around the central atom: each lone pair = 1, each bond (single, double, or triple) = 1",
              "Lone pairs and double bonds take more room -> squeeze nearby bond angles smaller",
              "Skeletal (bond-line) drawings: a C at every corner and line end; add H's so each C has 4 bonds",
              "Wedge = toward you, dashed wedge = away, plain line = in the page",
          ],
          C=[
              "VSEPR TABLE (domains, lone pairs: electron geometry / molecular geometry; angle; examples)\n"
              "* 2,0: linear / linear; 180 deg; CO2, HCN\n"
              "* 3,0: trigonal planar / trigonal planar; 120 deg; CH2O, SO3, NO3^-\n"
              "* 3,1: trigonal planar / bent; < 120 deg (~117 deg); O3, SO2\n"
              "* 4,0: tetrahedral / tetrahedral; 109.5 deg; CH4, NH4^+\n"
              "* 4,1: tetrahedral / trigonal pyramidal; ~107 deg; NH3, H3O^+\n"
              "* 4,2: tetrahedral / bent; ~104.5 deg; H2O, H2S\n"
              "* 5,0: trigonal bipyramidal / trigonal bipyramidal; 90 deg, 120 deg; PCl5\n"
              "* 6,0: octahedral / octahedral; 90 deg; SF6",
              "SHORTCUT FOR ORGANIC MOLECULES\n"
              "* C with 4 single bonds -> tetrahedral ~109 deg\n"
              "* C with one double -> trigonal planar ~120 deg\n"
              "* C with a triple or two doubles -> linear 180 deg\n"
              "* N with 3 single -> pyramidal ~107 deg\n"
              "* O with 2 single -> bent ~105 deg",
              "METHOD: Geometry of any atomic center\n"
              "1. Draw the Lewis structure.\n"
              "2. Count domains around that atom (lone pairs + bonded atoms).\n"
              "3. Domains -> electron geometry; then lone pairs -> molecular geometry (from the table).\n"
              "4. Adjust angles: smaller next to lone pairs or double bonds.\n"
              "5. Big molecules: repeat one center at a time.",
              "FUNCTIONAL GROUPS (class: group; structure)\n"
              "* Alcohol: hydroxyl; R-O-H\n"
              "* Aldehyde: aldehyde; R-CH=O\n"
              "* Ketone: ketone; R_1-C(=O)-R_2\n"
              "* Carboxylic acid: carboxyl; R-C(=O)-O-H\n"
              "* Ether: alkoxy; R_1-O-R_2\n"
              "* Amine: amine; R-N(R_1)(R_2), R's can be H\n"
              "* Aromatic: phenyl; 6-carbon ring with alternating double bonds",
          ]),
        U("3.8 Polarity",
          F=[
              "|delta| = |chi_A-chi_B|/(chi_A+chi_B)",
              "|delta| = Deltachi/(2*chi_AV)",
              "mu = |delta|*d",
              "mu (in C*m) = |delta|*(1.602x10^-19)*d, with d in meters",
              "1 Debye (D) = 3.335x10^-30 C*m",
          ],
          V=[
              ("delta", "partial charge in units of e (the more electronegative atom gets delta-, the other delta+, equal magnitude)"),
              ("chi_A, chi_B", "electronegativities of the two bonded atoms"),
              ("Deltachi", "their difference"),
              ("chi_AV", "their average"),
              ("mu", "bond dipole moment"),
              ("d", "bond length"),
              ("D", "Debye = 3.335x10^-30 C*m"),
          ],
          N=[
              "Dipole arrow points from delta+ toward delta- (direction electron density shifts)",
              "C-H bonds (Deltachi ~ 0.4) treated as nonpolar -> hydrocarbon chains are nonpolar",
              "Electrostatic potential maps: red = negative (e^- rich), blue = positive (e^- poor)",
          ],
          C=[
              "PAULING chi (check your book's table)\n"
              "* H 2.20, C 2.55, N 3.04, O 3.44, F 3.98\n"
              "* Cl 3.16, Br 2.96, I 2.66, S 2.58, P 2.19",
              "METHOD: Is the molecule polar?\n"
              "1. Draw the Lewis structure and get the 3D geometry (VSEPR).\n"
              "2. Mark delta+ and delta- on each bond using Deltachi; draw dipole arrows (longer for bigger Deltachi).\n"
              "3. Add the arrows as vectors (head-to-tail).\n"
              "4. Arrows cancel (symmetric shape, identical outer atoms: CO2, CH4, CCl4, SO3, BF3, SF6) -> nonpolar (mu = 0).\n"
              "5. Don't cancel (lone pairs on the central atom, or different outer atoms: H2O, NH3, SO2, O3, CHCl3, CH2O) -> polar.",
          ]),
    ],
})

# ---------------------------------------------------------------------
# 4. Unit 3: Predicting properties (IMFs, macromolecules, ionic networks)
# ---------------------------------------------------------------------
MODULES.append({
    "title": "4 U3 IMFs/Ionic",
    "full": "4. Unit 3: Predicting properties (IMFs, macromolecules, ionic networks)",
    "units": [
        U("4.1 Molecular or ionic",
          N=[
              "Only nonmetals -> molecular compound (discrete molecules held together by IMFs)",
              "Metal + nonmetal (Deltachi large, > ~2) -> ionic compound (network of ions, electrons transferred)",
              "Percent ionic character > 50% -> treat as ionic (NaCl ~ 80% ionic, delta ~ +/-0.8)",
          ]),
        U("4.2 IMFs",
          V=[
              ("IMF", "intermolecular force"),
          ],
          N=[
              "Polarizability (how easily e^- cloud distorts) increases with more electrons, larger size, and elongated/flat shape (more surface contact); branched/spherical -> less contact -> weaker dispersion",
              "Dispersion is usually the biggest contributor, even for polar molecules (dipole-dipole often < 20% of total)",
              "H-bond needs: H directly bonded to N, O, or F in one molecule + N, O, or F with a lone pair in another",
              "Stronger IMFs -> higher T_b, T_m, heat of vaporization, viscosity, surface tension; lower vapor pressure (less volatile)",
              "MIXING AND SOLUBILITY OF MOLECULAR SUBSTANCES\n"
              "* \"Like dissolves like\": mixing is favored when A-B interactions are about as strong as A-A and B-B\n"
              "* Mixing always increases configurations; it fails when one substance's own interactions are much stronger (water won't mix with hexane: H-bonds between water molecules would be lost)\n"
              "* PEC view: mixed state lower in E_p and more configurations -> soluble at all T; only one favorable -> solubility depends on T (higher T favors the more-configurations state)\n"
              "* Big differences in size, composition, or polarity -> immiscible",
          ],
          C=[
              "IMF TABLE (interaction: between; strength kJ/mol)\n"
              "* Dispersion (induced dipole-induced dipole, London): all molecules; 0.05-40\n"
              "* Dipole-induced dipole: polar + nonpolar; 2-10\n"
              "* Ion-induced dipole: ion + nonpolar; 3-15\n"
              "* Dipole-dipole: polar + polar; 5-25\n"
              "* Hydrogen bond: H on N/O/F + lone pair on another N/O/F; 10-40\n"
              "* Ion-dipole: ion + polar (e.g. salt in water); 4-600\n"
              "* Covalent bond (for comparison): atoms in a molecule; ~300-570",
              "METHOD: Rank boiling points (or viscosity, etc.)\n"
              "1. Draw each molecule; decide polar or nonpolar (Section 3.8); check for N-H, O-H, F-H.\n"
              "2. List IMFs present for each: all have dispersion; polar adds dipole-dipole; N/O/F-H adds H-bonding.\n"
              "3. If sizes are very different, the much larger molecule (more e^-, more surface) usually wins -- dispersion dominates.\n"
              "4. If sizes are similar: H-bonding > dipole-dipole > dispersion only.\n"
              "5. Same formula (isomers): straight chain > branched.\n"
              "6. Write the justification: \"X has stronger [type] forces because [more electrons / larger surface / polar / H-bonding], so more energy is needed to separate its molecules -> higher T_b.\"",
          ]),
        U("4.3 Macromolecules",
          V=[
              ("n", "number of repeat units in a polymer (subscript on the bracketed repeat unit)"),
              ("R", "amino acid side chain"),
          ],
          N=[
              "Polymer = many monomers joined by covalent bonds; repeat unit written in brackets with subscript n",
              "Functional groups that H-bond or are polar -> hydrophilic (wetted/dissolved by water); hydrocarbon groups -> hydrophobic",
              "Proteins: amino acids (-NH2 + -COOH + side chain R) joined by peptide bonds (water released)",
              "Primary structure = amino acid sequence; secondary = alpha-helix or beta-sheet held by H-bonds between N-H and C=O on the backbone; tertiary/quaternary = overall 3D fold and assembly of chains",
          ],
          C=[
              "STRUCTURAL CHANGE -> EFFECT\n"
              "* Longer chains: more contact points + tangling -> higher T_m, harder, more viscous\n"
              "* Linear (unbranched) chains: pack closer -> higher density, higher T_m (HDPE)\n"
              "* Short branches: chains slide past each other -> lower density (LDPE), lower viscosity\n"
              "* Long branches: entangle -> higher viscosity\n"
              "* Plasticizer added: small molecules space chains apart -> softer, more flexible\n"
              "* Cross-linking agent: covalent or strong links between chains -> rigid, harder (vulcanized rubber, S cross-links)\n"
              "* Many H-bonds between chains: strong, heat resistant (nylon, Kevlar)",
          ]),
        U("4.4 Ions/formula units",
          N=[
              "Metals lose valence e^- -> cation with the previous noble gas's configuration; nonmetals gain e^- until their valence shell is full -> anion with the next noble gas's configuration",
              "Transition metals: several possible charges -> Roman numeral in the name (Fe^3+ = iron(III), Cu^+ = copper(I))",
          ],
          C=[
              "USUAL ION CHARGE BY GROUP\n"
              "* Group 1: +1\n"
              "* Group 2: +2\n"
              "* Group 13: +3 (sometimes +1)\n"
              "* Group 15: -3\n"
              "* Group 16: -2\n"
              "* Group 17: -1",
              "COMMON POLYATOMIC IONS\n"
              "* hydroxide OH^-\n"
              "* nitrate NO3^-\n"
              "* carbonate CO3^2-\n"
              "* sulfate SO4^2-\n"
              "* phosphate PO4^3-\n"
              "* ammonium NH4^+\n"
              "* (also appear: cyanide CN^-, acetate CH3COO^-)",
              "METHOD: Formula unit from two elements or ions\n"
              "1. Write each ion with its charge.\n"
              "2. Find the smallest numbers that make total + charge = total - charge (criss-cross the charge magnitudes, then reduce).\n"
              "3. Use parentheses for more than one polyatomic ion: Ca3(PO4)2, Mg(NO3)2, Al2O3.",
              "UNIT CELL COUNTING (formula from a lattice picture)\n"
              "* corner = 1/8, edge = 1/4, face = 1/2, inside = 1\n"
              "* NaCl lattice: each ion has 6 opposite neighbors (FCC)\n"
              "* CsCl: each ion has 8 (BCC)",
          ]),
        U("4.5 Coulomb's law",
          F=[
              "F = K*q_1*q_2/r^2",
              "q = (charge number)*1.602x10^-19 C",
              "r ~ cation radius + anion radius",
              "F prop. to q_1*q_2/r^2",
          ],
          V=[
              ("F", "electrostatic force (N)"),
              ("K", "8.988x10^9 N*m^2/C^2"),
              ("q_1, q_2", "ion charges (C) = (charge number) x 1.602x10^-19 C"),
              ("r", "distance between ion centers (m) ~ cation radius + anion radius"),
          ],
          N=[
              "Bigger charges and smaller ions -> stronger attraction -> higher T_m, T_b, heat of fusion; separating ions costs 400-4000 kJ/mol",
              "Cations are smaller than their neutral atom; anions are larger; same-charge ions get bigger going down a group and right-to-left",
              "Brittle: a blow shifts layers so like charges line up and repel -> shatters",
              "Conduct only when molten or dissolved (ions free to move)",
          ],
          C=[
              "METHOD: Rank melting points of ionic compounds\n"
              "1. Write the ions and their charges for each compound.\n"
              "2. Compare charge products |q_1 x q_2| first: larger product -> higher T_m (MgO 2x2 > NaCl 1x1).\n"
              "3. If charges are equal, compare sizes: smaller ions (higher up the table) -> smaller r -> higher T_m (NaF > NaCl > NaBr; BeO > MgO > CaO > BaO).\n"
              "4. Justify with Coulomb's law: F prop. to q_1*q_2/r^2.",
          ]),
        U("4.6 Ionic solubility",
          F=[
              "NaCl(s) -> Na^+(aq) + Cl^-(aq)",
              "CaCl2(s) -> Ca^2+(aq) + 2 Cl^-(aq)",
          ],
          V=[
              ("(s)", "solid"),
              ("(aq)", "aqueous (dissolved in water)"),
          ],
          N=[
              "Dissolves if (a) ion-water interactions beat ion-ion interactions (lower E_p) and (b) mixing gives more configurations; one of two -> T-dependent; neither -> insoluble",
              "Small charges (+1, -1) -> usually soluble; both charges > 1 -> usually insoluble (high charges lock water molecules in place -> fewer configurations)",
              "Soluble -> strong electrolyte (fully dissociates, conducts); slightly soluble -> weak electrolyte",
          ],
          C=[
              "MOSTLY SOLUBLE (exceptions = insoluble)\n"
              "* F^-: insoluble with Mg^2+, Ca^2+ (alkaline earths), Pb^2+\n"
              "* Cl^-, Br^-, I^-: insoluble with Ag^+, Hg2^2+, Pb^2+\n"
              "* NO3^-: no exceptions\n"
              "* SO4^2-: insoluble with Sr^2+, Ba^2+, Hg2^2+, Pb^2+",
              "MOSTLY INSOLUBLE (exceptions = soluble)\n"
              "* S^2-: soluble with NH4^+, alkali metals, alkaline earths\n"
              "* OH^-: soluble with alkali metals, NH4^+, Ca^2+, Sr^2+, Ba^2+\n"
              "* CO3^2-: soluble with NH4^+, alkali metals\n"
              "* PO4^3-: soluble with NH4^+, alkali metals",
              "METHOD: Will a precipitate form when two solutions mix?\n"
              "1. Write all ions present after mixing.\n"
              "2. Swap partners: pair each cation with the other solution's anion.\n"
              "3. Check each new pair in the tables; an insoluble pair = the precipitate.\n"
              "4. Write it with (s), everything else (aq).",
          ]),
    ],
})

# ---------------------------------------------------------------------
# 5. Unit 4: Reactions, stoichiometry, energy
# ---------------------------------------------------------------------
MODULES.append({
    "title": "5 U4 Reactions/Energy",
    "full": "5. Unit 4: Reactions, stoichiometry, energy",
    "units": [
        U("5.1 Change/assumptions",
          N=[
              "Chemical change = new substance with different composition (burning, rusting); physical change = same substance (boiling, dissolving sugar)",
              "Reactions: mass is conserved, reactants combine in fixed ratios, energy is always transferred, rates vary, some go to completion and some reach equilibrium",
          ],
          C=[
              "THE SIX REACTION ASSUMPTIONS\n"
              "1. Atoms are rearranged (bonds broken and formed); atoms are conserved.\n"
              "2. Electrons redistribute -> internal potential energy E_p changes -> energy is absorbed or released.\n"
              "3. Particles must collide; more collisions -> faster.\n"
              "4. Collisions must have the right orientation (configuration effectiveness); simpler molecules / fewer particles -> faster.\n"
              "5. Colliding particles need at least the activation energy E_a to reach the transition state.\n"
              "6. Reactions run forward and backward; equilibrium when both rates are equal.",
          ]),
        U("5.2 Energy diagrams",
          F=[
              "DeltaH_rxn = E_p,products - E_p,reactants",
              "DeltaH_rxn = E_a,forward - E_a,reverse",
              "At equilibrium: [prod]/[react] = P_f/P_b",
              "lambda_max = h*c*N_A/E_a",
          ],
          V=[
              ("DeltaH_rxn", "heat of reaction (kJ/mol)"),
              ("E_p", "internal potential energy"),
              ("E_a", "activation energy (height of the barrier from the starting side)"),
              ("lambda_max", "longest wavelength that can activate a photo-activated reaction"),
              ("[prod]/[react]", "ratio of products to reactants at equilibrium"),
              ("P_f, P_b", "probability of the forward / backward step"),
          ],
          N=[
              "EXOTHERMIC: products lower, DeltaH < 0, surroundings warm up, E_a(forward) < E_a(reverse) -> tends to be product-favored",
              "ENDOTHERMIC: products higher, DeltaH > 0, surroundings cool, E_a(forward) > E_a(reverse) -> tends to be reactant-favored",
              "Faster reaction: higher T (more particles above E_a), higher concentration or pressure (more collisions), lower E_a (catalyst gives an alternate path), simpler reacting particles (more effective orientations)",
              "Equilibrium extent: [products]/[reactants] at equilibrium = (probability forward) / (probability backward); e.g. 60% A->B and 30% B->A per step -> B/A = 2 -> 1/3 mol A, 2/3 mol B from 1 mol A",
              "Photo-activated reaction: the longest wavelength that works has photon energy = E_a per molecule -> lambda_max = h*c*N_A/E_a (O2 splitting, E_a = 498.5 kJ/mol -> ~ 240 nm)",
          ],
          C=[
              "METHOD: Draw an energy diagram\n"
              "1. x-axis = reaction path, y-axis = E_p.\n"
              "2. Put reactants on the left and products on the right; place products lower (exothermic) or higher (endothermic) by |DeltaH|.\n"
              "3. Draw a hump; its height above the reactants = E_a(forward), above the products = E_a(reverse).\n"
              "4. Multi-step: one hump per step, with intermediates in the valleys between.",
          ]),
        U("5.3 Balancing",
          N=[
              "Combustion of C_xH_y(O_z): products CO2 and H2O; e.g. C3H8 + 5 O2 -> 3 CO2 + 4 H2O; 2 C8H18 + 25 O2 -> 16 CO2 + 18 H2O",
              "Coefficients = mole ratios (and particle ratios), not mass ratios",
          ],
          C=[
              "METHOD: Balance an equation\n"
              "1. Write correct formulas (never change subscripts).\n"
              "2. Balance the element in the most complex molecule first (usually C, then H).\n"
              "3. Balance O (or the element found alone, like O2) last; use a fraction if needed, then multiply everything to clear it.\n"
              "4. Reduce coefficients to the smallest whole numbers; check every atom type.",
          ]),
        U("5.4 Stoichiometry",
          F=[
              "n_B = n_A*(nu_B/nu_A)",
              "m_B = (m_A/M_A)*(nu_B/nu_A)*M_B",
              "Percent yield = (actual yield/theoretical yield)*100",
              "EF_CO2 = (%C/100)*(44.01/12.01)",
              "AFR = m_air/m_fuel = (m_O2/0.233)/m_fuel",
          ],
          V=[
              ("n_A, n_B", "moles of substances A and B"),
              ("nu_A, nu_B", "their coefficients in the balanced equation"),
              ("m", "mass (g)"),
              ("M", "molar mass (g/mol)"),
              ("EF", "kg CO2 released per kg fuel burned (emission factor)"),
              ("%C", "mass percent carbon in the fuel"),
              ("m_air, m_fuel", "masses of air and fuel (g)"),
              ("AFR", "air-fuel mass ratio"),
              ("m_O2", "grams of O2 needed to burn m_fuel grams completely"),
              ("air", "21% O2 / 79% N2 by moles = 23.3% O2 / 76.7% N2 by mass"),
              ("rho", "density (liquid: m = rho x V)"),
          ],
          N=[
              "Octane: EF ~ 3.08 kg CO2/kg; gasoline stoichiometric AFR ~ 14.7",
              "AFR below stoichiometric = \"rich\" (fuel in excess, O2 limiting -> CO and unburned fuel in exhaust); above = \"lean\" (O2 in excess)",
              "Higher %C (bigger molecules, more double/triple bonds) -> higher EF",
          ],
          C=[
              "METHOD: Grams of A -> grams of B\n"
              "1. Balance the equation.\n"
              "2. Grams A / M_A -> mol A (liquid by volume: m = rho x V; gas: n = PV/RT; solution: n = [A] x V).\n"
              "3. mol A x (coefficient B / coefficient A) -> mol B.\n"
              "4. mol B x M_B -> grams B.",
              "METHOD: Limiting reactant and theoretical yield\n"
              "1. Convert every reactant to moles.\n"
              "2. Actual ratio = mol X / mol Y; stoichiometric ratio = coef X / coef Y.\n"
              "3. Actual < stoichiometric -> X (numerator) is limiting. Actual > stoichiometric -> Y is limiting. Equal -> both used up.\n"
              "4. (Shortcut: mol / coefficient for each reactant; smallest value = limiting.)\n"
              "5. Theoretical yield = product calculated from the limiting reactant only.\n"
              "6. Excess left over = initial mol excess - mol excess used (from the ratio).",
          ]),
        U("5.5 Bond energy & heat",
          F=[
              "DeltaH_rxn = SUM BE(bonds broken, reactants) - SUM BE(bonds formed, products)",
              "E_p of a molecule (vs free atoms) = -SUM BE of its bonds",
              "Per gram of fuel: DeltaH/(coefficient*M_fuel)",
              "For a given amount: DeltaH*(mol reacted/coefficient)",
              "q = m*c*DeltaT",
              "DeltaT = T_final - T_initial",
          ],
          V=[
              ("DeltaH_rxn", "heat of reaction (kJ per mole of reaction as written)"),
              ("BE", "average bond energy (kJ/mol); breaking bonds absorbs energy (+), forming bonds releases energy (-)"),
              ("q", "heat absorbed (+) or released (-) by a sample (J)"),
              ("M_fuel", "molar mass of the fuel (g/mol)"),
              ("m", "mass (g)"),
              ("c", "specific heat capacity (J/(g*degC)), energy to raise 1 g by 1 degC; water ~ 4.184"),
              ("DeltaT", "T_final - T_initial (degC or K)"),
          ],
          N=[
              "Stronger bond = deeper E_p well = more energy to break = more released when formed; bonds don't \"store\" energy",
              "E_p of a molecule relative to free atoms = -SUM BE of its bonds (CH4: -4 x 414 = -1656 kJ/mol)",
              "Sign convention: energy released by the system is negative (q = -802 kJ/mol for CH4 combustion)",
          ],
          C=[
              "BOND ENERGIES (all in kJ/mol)\n"
              "* H-H 436, C-H 414, C-C 347\n"
              "* C=C 611, C#C 737\n"
              "* C-Cl 339, C-N 305, C=N 615\n"
              "* C-O 360, C=O 736 (799 in CO2)\n"
              "* C-S 259, N-H 389, N-N 163\n"
              "* N#N 946, N-O 201, N=O 607\n"
              "* O-H 464, O-O 142, O=O 498\n"
              "* S-H 368",
              "METHOD: Estimate DeltaH_rxn\n"
              "1. Balance the equation and draw Lewis structures of every species.\n"
              "2. Count every bond broken in the reactants (x coefficient); add their BEs.\n"
              "3. Count every bond formed in the products (x coefficient); add their BEs.\n"
              "4. DeltaH = broken - formed. Negative -> exothermic. Example: CH4 + 2 O2 -> CO2 + 2 H2O: 4(414) + 2(498) - 2(799) - 4(464) = -802 kJ.\n"
              "5. Per gram of fuel: DeltaH / (coefficient x M of fuel). For a given amount: DeltaH x (mol reacted / coefficient).",
          ]),
    ],
})


NOTATION_KEY = [
    "HOW TO READ THE MATH\n"
    "* x_1 = x sub 1 (subscript)\n"
    "* x^2 = x squared (power)\n"
    "* 6.022x10^23 = 6.022 times 10 to the 23 (type 6.022E23 on the calculator)\n"
    "* * = multiply, / = divide\n"
    "* (1/2)*m*<v>^2 = one half times m times (average v) squared\n"
    "* SUM = add them all up (Greek capital sigma)\n"
    "* |x| = absolute value of x\n"
    "* ~ = approximately\n"
    "* prop. to = proportional to\n"
    "* -> = gives / leads to; <-> = both ways",
    "GREEK LETTERS\n"
    "* Delta = change in (DeltaH, DeltaT, DeltaE)\n"
    "* delta = partial charge (delta+, delta-)\n"
    "* lambda = wavelength\n"
    "* nu = frequency (nu_A in stoichiometry = coefficient of A)\n"
    "* nu~ = wavenumber (nu with a tilde)\n"
    "* chi = electronegativity\n"
    "* mu = dipole moment; u in units = micro (ug)\n"
    "* rho = density\n"
    "* alpha, beta = alpha-helix, beta-sheet",
    "CHEMISTRY SYMBOLS\n"
    "* H2O, CO2: digits after an element are subscripts\n"
    "* Na^+, Cl^-, Ca^2+, SO4^2- = ion charges\n"
    "* C-H single, C=O double, C#N triple bond\n"
    "* Cl-35 = chlorine-35 isotope\n"
    "* M^+ = molecular ion peak\n"
    "* e^- = electron\n"
    "* degC = degrees Celsius; deg = angle degrees\n"
    "* <E_k> = average kinetic energy",
    "NAVIGATION\n"
    "* Type a number + [enter] to open an item\n"
    "* [enter] alone = next page\n"
    "* - (minus) then [enter] = previous page\n"
    "* 0 [enter] = go back one level\n"
    "* 00 [enter] = jump to main menu\n"
    "* [on] = break / quit the program",
]


# Full section titles from the sheet (menus use the short versions).
FULL_TITLES = [
    "0.1 Constants",
    "0.2 Conversions",
    "0.3 Factor-label method (works for every unit problem)",
    "1.1 Differentiating characteristics",
    "1.2 Heating / cooling curves (T vs t) and DeltaE vs T",
    "1.3 Phase diagrams (P vs T)",
    "1.4 Vapor pressure and boiling",
    "1.5 Separation techniques",
    "1.6 Particulate model of matter",
    "1.7 Ideal gases",
    "1.8 Potential energy and phase changes",
    "1.9 PEC (potential energy-configuration) diagrams",
    "1.10 Emergent properties and common traps",
    "2.1 Classifying matter (+ naming binary compounds)",
    "2.2 Mass <-> moles <-> particles",
    "2.3 Solutions and concentration",
    "2.4 Ideal gas law (molar form) (+ other Unit 1 ratio problems)",
    "2.5 Subatomic model",
    "2.6 Average atomic mass from isotopes",
    "2.7 Reading mass spectra",
    "2.8 Empirical and molecular formulas (combustion analysis) (+ mass percent from a formula)",
    "3.1 EM radiation and photons",
    "3.2 Quantization, spectra, photoelectric effect, PES",
    "3.3 Electron configurations and periodic trends",
    "3.4 Valence (bonding capacity)",
    "3.5 Lewis structures",
    "3.6 IR spectroscopy (connectivity)",
    "3.7 VSEPR geometry (+ skeletal drawings, functional groups)",
    "3.8 Bond and molecular polarity",
    "4.1 Molecular or ionic?",
    "4.2 Intermolecular forces (IMFs) (+ mixing and solubility of molecular substances)",
    "4.3 Macromolecules and polymers",
    "4.4 Forming ions and formula units",
    "4.5 Coulomb's law and ionic properties",
    "4.6 Solubility of ionic compounds",
    "5.1 Chemical vs physical change; the six reaction assumptions",
    "5.2 Energy diagrams, rate, and extent",
    "5.3 Balancing equations",
    "5.4 Stoichiometry (+ CO2 emission factor and air-fuel ratio)",
    "5.5 Bond energies and heat of reaction (+ heat and temperature)",
]
