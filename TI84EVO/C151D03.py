# C151D03: data for CHEM151. Don't run this file.
D=(
"SEPARATION TECHNIQUES (technique: differentiating property -> what "
"separates)\n* Filtration: phase (solid vs fluid) -> solid from liqui"
"d/gas\n* Crystallization: solubility (changes with T or concentratio"
"n) -> a pure solid out of a solution\n* Distillation: boiling point "
"-> liquids; most volatile comes out first\n* Fractional distillation"
": boiling point (close values) -> column hot at bottom, cool at "
"top; most volatile condenses highest\n* Chromatography: strength "
"of attraction to the stationary phase -> weakly attracted substances"
" exit first (shorter retention time)\n\nMETHOD: Design a separation "
"(e.g. a mixture of gases or liquids)\n1. List each component's T_m "
"and T_b (or VP curve).\n2. Pick the property that differs most -> "
"that's the differentiating characteristic.\n3. Order components "
"by boiling point; when cooling a gas mixture, the highest T_b conden"
"ses first; when heating a liquid, the lowest T_b boils off first.\n4"
". Give the temperature for each step, set between consecutive boilin"
"g points.\n5. State the outcome of each step (what's collected, "
"what remains).\n\nMETHOD: Fractional distillation column (trays)\n1."
" Sort all substances by T_b.\n2. For each fraction you want, find "
"the T_b range it needs (e.g. \"liquid between 5 degC and 38 degC\" "
"-> needs T_m < 5 degC and T_b > 38 degC).\n3. Place a tray at a "
"temperature between the last substance of one fraction and the first"
" substance of the next.\n4. Number of trays = number of boundaries "
"between fractions inside the column; top exhaust = gases more volati"
"le than the top T; bottom = everything above the bottom T.\n5. List "
"which substances end up in each fraction.",
"* <E_k> = (1/2)*m*<v>^2",
"* <E_k> = average kinetic energy per particle (J)\n* m = mass of "
"one particle (kg)\n* <v> = average particle speed (m/s)",
"PARTICULATE MODEL OF MATTER\n1. Matter is made of tiny (~1 nm) ident"
"ical particles.\n2. Particles move constantly and randomly through "
"empty space.\n3. Particles attract at long range and repel at short "
"range.\n\n* T IS A MEASURE OF <E_k>. Same T -> same <E_k>, regardles"
"s of substance or phase\n* At the same T: lighter particles move "
"faster (m down -> v up)\n* At a triple point all three phases have "
"the SAME average speed (same T)\n* Higher T -> speed distribution "
"shifts right and flattens (more fast particles)",
"* P = k_B*N*T/V\n* N = P*V/(k_B*T)\n* P prop. to T (const N, V)\n* "
"P prop. to N (const T, V)\n* P prop. to 1/V (const N, T)\n* Gas "
"changes conditions (N fixed): P_1*V_1/T_1 = P_2*V_2/T_2\n* V_2 = "
"V_1*(P_1/P_2)*(T_2/T_1)",
"* P = pressure (Pa)\n* N = number of particles\n* T = absolute tempe"
"rature (K)\n* V = volume (m^3)\n* k_B = Boltzmann constant = 1.380x1"
"0^-23 J/K\n* X_1, X_2 = subscript 1 = initial state, 2 = final state"
"; T in K; P and V in any matching units",
"* Same T, P, V -> same N for any gas (Avogadro's hypothesis); P "
"does NOT depend on particle mass\n* Ideal behavior: high T, low "
"P (particles far apart, interactions negligible)\n* REAL GASES: "
"repulsion (particle size) -> less free volume -> P HIGHER than ideal"
"; attraction -> particles hit walls less -> P LOWER than ideal. "
"Deviations grow near condensation (low T, high P).",
)
