# C151D09: data for CHEM151. Don't run this file.
D=(
"* lambda = wavelength (m)\n* nu = frequency (s^-1 = Hz)\n* c = speed"
" of light = 3.00x10^8 m/s (3.00x10^10 cm/s for wavenumbers, lambda "
"in cm)\n* E = energy of ONE photon (J)\n* h = Planck's constant "
"= 6.626x10^-34 J*s\n* nu~ = wavenumber (cm^-1, IR spectra)\n* E_mola"
"r = energy per mole of photons (J/mol)",
"* For wavenumbers use c = 3.00x10^10 cm/s (lambda in cm)\n* Longer "
"lambda <-> lower nu <-> lower E",
"METHOD: lambda <-> nu <-> E (per photon and per mole)\n1. Convert "
"lambda to meters (nm x 10^-9) or nu~ to m^-1 (cm^-1 x 100).\n2. "
"nu = c/lambda; E = h*nu (J per photon).\n3. x N_A, divide by 1000 "
"-> kJ/mol.\n4. Backwards (given DeltaE): per photon E = DeltaE(J/mol"
")/N_A; lambda = hc/E; name the region.\n\nEM REGIONS, long lambda "
"-> short lambda (approx lambda; energy kJ/mol; what it does)\n* "
"Radio / microwave: m to mm; 10^-3 to 10^-1; rotational transitions\n"
"* Infrared (IR): ~1 mm to 700 nm; 10^-1 to 10^2; vibrational transit"
"ions (stretch, bend)\n* Visible: 700 nm (red) to 400 nm (violet); "
"~170 to 300; electron excitation\n* Ultraviolet (UV): 400 to 10 "
"nm; 10^2 to 10^3; electron excitation, bond breaking, ionization\n* "
"X-ray / gamma: < 10 nm; > 10^4; removes core electrons",
"* |DeltaE| = E_upper - E_lower = h*nu\n* E_I = h*nu - E_k",
"* DeltaE = energy gap between two levels (J per photon)\n* E_upper, "
"E_lower = energies of the upper and lower levels\n* E_I = ionization"
" energy (energy to remove an electron)\n* E_k = kinetic energy of "
"the ejected electron",
"* Energy transfer only in whole photons; atoms/molecules only exist "
"in discrete energy levels\n* Absorption and emission lines of an "
"element appear at the SAME lambda; each line = one transition\n* "
"Photoelectric effect: ejection only if h*nu > threshold; KE of elect"
"ron grows with nu, not with intensity (intensity = number of photons"
")\n* Ground state = lowest levels filled; excited state = electron "
"promoted\n* Electron as a wave: smaller space -> shorter wavelength "
"-> higher kinetic energy; delocalization (spreading out, e.g. bondin"
"g) lowers kinetic energy\n* Blackbody: hotter object -> peak shifts "
"to shorter lambda (red -> white -> blue) and more total energy\n* "
"Molecular bands are broad because neighboring molecules shift energy"
" levels slightly",
"* n = shell number\n* Z = atomic number (= number of e^- in a neutra"
"l atom)\n* chi = electronegativity",
"* Each orbital holds 2 e^- with opposite spins (Pauli); e^- occupy "
"empty orbitals singly before pairing\n* Noble gas notation: [previou"
"s noble gas] + outer electrons (Ge = [Ar] 4s^2 3d^10 4p^2)\n* Valenc"
"e electrons = outermost s + p electrons (group 1-2: group number; "
"group 13-18: group number - 10)\n* Big jump in radius and drop in "
"ionization energy when a new shell starts (He -> Li, Ne -> Na)",
)
