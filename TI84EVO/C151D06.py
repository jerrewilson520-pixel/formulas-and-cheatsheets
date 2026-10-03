# C151D06: data for CHEM151. Don't run this file.
D=(
"* PV = nRT = (m/M)*R*T\n* M = m*R*T/(P*V)\n* d = P*M/(R*T)\n* n/V "
"= P/(R*T)\n* Other Unit 1 ratio problems: Percent increase = (new-ol"
"d)/old*100\n* Molecules of B per molecule of A = (m_B/M_B)/(m_A/M_A)"
"\n* GWP per molecule = (GWP per gram)*M(gas)/M(CO2)",
"* P = pressure (atm)\n* V = volume (L)\n* n = moles of gas\n* R "
"= 0.08206 L*atm/(K*mol)\n* T = temperature (K)\n* m = mass of gas "
"(g)\n* M = molar mass (g/mol)\n* d = gas density (g/L)\n* n/V = "
"molar concentration of gas (mol/L)\n* GWP = global warming potential"
"; GWP per molecule = how many CO2 molecules equal one molecule of "
"the gas",
"* 1 mol of ideal gas at STP (0 degC, 1 atm) = 22.41 L; at 25 degC, "
"1 atm = 24.47 L\n* Volume % of a gas in a mixture = mole % (e.g. "
"air is 78.08% N2 by volume -> 0.7808 of the moles)",
"METHOD: Identify an unknown gas\n1. Convert m to g, V to L, P to "
"atm, T to K.\n2. M = mRT / PV.\n3. Match M to a formula (e.g. 28 "
"g/mol from C and O -> CO).\n\nMETHOD: Convert pollutant concentratio"
"ns (mg/m^3 <-> mol/L <-> molecules/mL <-> ppmv)\n1. mg/m^3 -> g/L: "
"x (1 g / 1000 mg) x (1 m^3 / 1000 L) -> overall divide by 10^6.\n2. "
"g/L -> mol/L: divide by M.\n3. mol/L -> molecules/mL: x N_A, then "
"divide by 1000.\n4. To ppmv: moles of air per L = P / RT; mole fract"
"ion = (mol pollutant/L) / (mol air/L); ppmv = mole fraction x 10^6.\n"
"5. Changing T at fixed mole fraction: gas concentration in mol/L "
"scales by T_1/T_2 (colder -> more concentrated).",
"* A = Z + N_n\n* charge = Z - (#e^-)",
"* A = mass number (protons + neutrons)\n* Z = atomic number = number"
" of protons (defines the element)\n* N_n = number of neutrons\n* "
"#e^- = number of electrons",
"* Isotopes: same Z, different neutrons (written with A as superscrip"
"t and Z as subscript, e.g. B-10 and B-11)\n* Ions: neutral atom "
"loses e^- -> cation (+), gains e^- -> anion (-); Z never changes\n* "
"Nucleus radius ~ 10^-14 m vs atom ~ 10^-10 m; mostly empty space "
"(Rutherford's gold foil)\n* amu scale set by carbon-12 = exactly "
"12 amu",
"SUBATOMIC PARTICLES (charge; mass; location)\n* Proton p^+: +1 (1.60"
"2x10^-19 C); 1.673x10^-27 kg; nucleus\n* Neutron n^0: 0; 1.675x10^-2"
"7 kg; nucleus\n* Electron e^-: -1; 9.109x10^-31 kg; around nucleus",
"* r.a.m. = SUM(isotope mass * %abundance)/100\n* Two isotopes, only "
"average known: x*m_1 + (1-x)*m_2 = average; solve for x",
"* r.a.m. = average relative atomic mass (amu = g/mol)\n* % abundance"
" = percent of atoms that are that isotope\n* x = fractional abundanc"
"e of isotope 1 (1 - x for isotope 2)\n* m_1, m_2 = masses of the "
"two isotopes",
"METHOD: Average atomic mass from isotopes\n1. Read each isotope's "
"mass (m/q) and % abundance from the spectrum.\n2. Multiply each "
"mass by its %; add; divide by 100.\n3. Two isotopes and only the "
"average known: x(m_1) + (1 - x)(m_2) = average, solve for x.\n4. "
"Check: the answer should sit closer to the more abundant isotope.",
"* Isotope pattern of X2: P(light-light) = f_L^2\n* P(light-heavy) "
"= 2*f_L*f_H\n* P(heavy-heavy) = f_H^2",
"* m/q = x-axis: mass-to-charge (~ mass of a +1 ion)\n* M^+ = molecul"
"ar ion (highest-m/q major peak)\n* f = fractional abundance\n* f_L, "
"f_H = fractional abundance of light / heavy isotope",
)
