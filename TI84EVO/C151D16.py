# C151D16: data for CHEM151. Don't run this file.
D=(
"* DeltaH_rxn = heat of reaction (kJ/mol)\n* E_p = internal potential"
" energy\n* E_a = activation energy (height of the barrier from the "
"starting side)\n* lambda_max = longest wavelength that can activate "
"a photo-activated reaction\n* [prod]/[react] = ratio of products "
"to reactants at equilibrium\n* P_f, P_b = probability of the forward"
" / backward step",
"* EXOTHERMIC: products lower, DeltaH < 0, surroundings warm up, "
"E_a(forward) < E_a(reverse) -> tends to be product-favored\n* ENDOTH"
"ERMIC: products higher, DeltaH > 0, surroundings cool, E_a(forward) "
"> E_a(reverse) -> tends to be reactant-favored\n* Faster reaction: "
"higher T (more particles above E_a), higher concentration or pressur"
"e (more collisions), lower E_a (catalyst gives an alternate path), "
"simpler reacting particles (more effective orientations)\n* Equilibr"
"ium extent: [products]/[reactants] at equilibrium = (probability "
"forward) / (probability backward); e.g. 60% A->B and 30% B->A per "
"step -> B/A = 2 -> 1/3 mol A, 2/3 mol B from 1 mol A\n* Photo-activa"
"ted reaction: the longest wavelength that works has photon energy "
"= E_a per molecule -> lambda_max = h*c*N_A/E_a (O2 splitting, E_a "
"= 498.5 kJ/mol -> ~ 240 nm)",
"METHOD: Draw an energy diagram\n1. x-axis = reaction path, y-axis "
"= E_p.\n2. Put reactants on the left and products on the right; "
"place products lower (exothermic) or higher (endothermic) by |DeltaH"
"|.\n3. Draw a hump; its height above the reactants = E_a(forward), "
"above the products = E_a(reverse).\n4. Multi-step: one hump per "
"step, with intermediates in the valleys between.",
"* Combustion of C_xH_y(O_z): products CO2 and H2O; e.g. C3H8 + 5 "
"O2 -> 3 CO2 + 4 H2O; 2 C8H18 + 25 O2 -> 16 CO2 + 18 H2O\n* Coefficie"
"nts = mole ratios (and particle ratios), not mass ratios",
"METHOD: Balance an equation\n1. Write correct formulas (never change"
" subscripts).\n2. Balance the element in the most complex molecule "
"first (usually C, then H).\n3. Balance O (or the element found alone"
", like O2) last; use a fraction if needed, then multiply everything "
"to clear it.\n4. Reduce coefficients to the smallest whole numbers; "
"check every atom type.",
"* n_B = n_A*(nu_B/nu_A)\n* m_B = (m_A/M_A)*(nu_B/nu_A)*M_B\n* Percen"
"t yield = (actual yield/theoretical yield)*100\n* EF_CO2 = (%C/100)*"
"(44.01/12.01)\n* AFR = m_air/m_fuel = (m_O2/0.233)/m_fuel",
"* n_A, n_B = moles of substances A and B\n* nu_A, nu_B = their coeff"
"icients in the balanced equation\n* m = mass (g)\n* M = molar mass "
"(g/mol)\n* EF = kg CO2 released per kg fuel burned (emission factor)"
"\n* %C = mass percent carbon in the fuel\n* m_air, m_fuel = masses "
"of air and fuel (g)\n* AFR = air-fuel mass ratio\n* m_O2 = grams "
"of O2 needed to burn m_fuel grams completely\n* air = 21% O2 / 79% "
"N2 by moles = 23.3% O2 / 76.7% N2 by mass\n* rho = density (liquid: "
"m = rho x V)",
"* Octane: EF ~ 3.08 kg CO2/kg; gasoline stoichiometric AFR ~ 14.7\n*"
" AFR below stoichiometric = \"rich\" (fuel in excess, O2 limiting "
"-> CO and unburned fuel in exhaust); above = \"lean\" (O2 in excess)"
"\n* Higher %C (bigger molecules, more double/triple bonds) -> higher"
" EF",
)
