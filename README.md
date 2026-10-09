# The BCT Superfluid Lattice Model, and its audit

> **Status, October 2026.** Most of BCT did not survive its own audit. What this page used
> to claim (that BCT derives the fine-structure constant, the particle masses, light and
> gravity from geometry, with zero free parameters) has been tested and retired. This page
> says why the idea looked so good, how it was tested, and what is left.

---

## What BCT was

In 2026 Michel Robert Cabrié, an independent artist in Barrys Reef, Victoria, built BCT in
a few intense months. The idea: the vacuum is a superfluid arranged as a body-centred
tetragonal lattice at c/a = √2 (the same arrangement as stacked spheres, FCC), and the sizes
of the gaps between the spheres, r_oct = (√2−1)/2 and r_tet = (√6−2)/4, fix the constants
of physics.

It grew fast: hundreds of Letters, appendices, volumes and claimed predictions, published on
Zenodo and written with the help of AI models.

## Why it looked beautiful

Start with oranges. Stack spheres as tightly as they will go and you get the greengrocer's
pyramid. Kepler guessed it was the densest packing possible, and Thomas Hales proved him
right. Seen from another angle, the same stack is a body-centred tetragonal lattice whose
height is exactly √2 times its width.

Between the spheres sit two kinds of gap, an octahedral one and a tetrahedral one, and their
sizes are exact: (√2−1)/2 and (√6−2)/4 of a sphere's diameter. Multiply the two and divide by
π, and you get 0.00741, about 1/135. That is within 1.5% of the fine-structure constant,
1/137, the number that sets the strength of light and charge and that physicists have puzzled
over for a century.

The picture around it was old and respectable. The vacuum as a superfluid is an idea serious
physicists have developed (Grigory Volovik's *The Universe in a Helium Droplet*). In that
picture light is a ripple in the fluid, and electric charge is a whirlpool that can only wind
a whole number of times, which gives charge in whole units for free. The four-dimensional
version of the lattice, D4, has a famous three-fold symmetry called triality, which looked
like a reason for the three generations of particles. And formula after formula built from
these numbers landed close to measured constants.

For a few months it looked as if the universe might be made of stacked spheres. Michel, and
the AI models helping him, believed it.

The geometry is still beautiful, and it is still true. What failed was the step from
beautiful numbers to physics. With two exact gap sizes, π and small whole numbers to play
with, you can build so many formulas that some will land close to almost any constant: 113
simple ones land within 1% of 137.036. A close match on its own proves nothing. Telling a
real derivation from a lucky match is what the audit was for.

## How it was tested

From September 2026 the claims went through a public audit, the Cold Ledger:

- every question gets a **card** that fixes the method and the pass and fail lines in advance;
- the card is **fingerprinted (SHA-256) and committed here before it runs**, so it cannot be
  changed after the fact;
- it is **run blind** in a fresh session, and negative results are published like positive ones.

The cards, code, data and results are in
[audit/gates](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates).
The audit is run with Claude (Anthropic) under this protocol.

## What the audit found

**Retired**

- **Light.** BCT's written field is a single phase at each lattice site. That cannot carry
  light's two polarisations, and the routes around it were closed one by one
  ([LINK](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/LINK),
  [XI](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/XI) and others).
- **Gravity.** Every route examined was closed
  ([PV](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/PV) and others).
- **Quantum mechanics.** BCT restates it in fluid language; it does not derive it
  ([MAD](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/MAD)).
- **The numbers.** BCT's matches to measured constants, 1/137 included, are about what a
  formula search of that size finds by chance, and none of the predictions presented as
  derived carries real statistical weight
  ([PRED](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/PRED),
  [PRED2](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/PRED2)).
- **Why 1/137.** Three routes to derive it were tested in October 2026. None does
  ([SPECTRUM2](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/SPECTRUM2),
  [CRIT](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/CRIT)).
- **c/a = √2** is a choice (close packing), not something the geometry forces.
- **Masses, mixing angles, the particle content and the "Chain of Necessity"** are fits or
  imports, not derivations
  ([RANK](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/RANK),
  [HERM](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/HERM),
  [CA-FLAVOUR](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/CA-FLAVOUR)).

**What is left**

- **The geometry.** The void radii are correct, and they are classical crystallography,
  known long before BCT.
- **Charge comes in whole units** because a vortex winds a whole number of times. Correct,
  and standard topology rather than new.
- **One new number.** The tipping point of lattice electromagnetism (compact U(1), Wilson
  action) on the D4 lattice, the four-dimensional lattice whose slices are the BCT/FCC
  packing: **β_c = 0.615 ± 0.001** (1.230 ± 0.003 in Katz and Nógrádi's normalisation), a
  first-order transition. It was measured by two independent programs, the second written
  blind to the first, and does not appear in the literature we searched
  ([CRIT](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/CRIT),
  [CRIT2](https://github.com/zerofreeparameters-code/BCT-Programme/tree/main/audit/gates/CRIT2)).
- **The method.** The audit record itself, kills included.

Some September and October results are still being moved into this repository. Until they
are, they live in the project's working notes, and the list above will grow.

## Older material

The Letters, appendices, volumes, patents, outreach posts and the book *Accidentally Solved*
were written before the audit and make claims that have since been retired. They stay
available as a record of what was tried, not as results. Where they disagree with
`audit/`, the audit is right.

- Zenodo records: [search](https://zenodo.org/search?q=cabri%C3%A9&sort=mostrecent)
- Published works index: [Master Index](https://zerofreeparameters-code.github.io/BCT-Programme/BCT_MasterIndex_live.html) (pre-audit)
- Book: [*Accidentally Solved*](https://www.amazon.com.au/dp/B0F3J2K9LM) (pre-audit)
- The BCT Ethical Patent Licence ([EPL_LICENCE.md](EPL_LICENCE.md)) still applies to the
  material here: free for humanitarian, educational and wildlife-conservation use; the
  Birdseed Clause gives anyone feeding wildlife free access; no military use, ever.

## About

**Michel Robert Cabrié** is an artist, not a physicist, in Barrys Reef, Victoria, Australia
(pop. ~28). He built a freshwater pond for the endangered Gang Gang Cockatoos, built BCT,
and is now auditing it in public.

- Email: ZeroFreeParameters@gmail.com
- ORCID: [0009-0007-9561-9859](https://orcid.org/0009-0007-9561-9859)
- Writing: [substack.com/@michelcabrie](https://substack.com/@michelcabrie)

## Acknowledgements

To the **Gang Gang Cockatoos** (*Callocephalon fimbriatum*) who visit the pond in Barrys Reef
every day; their declining numbers are a reminder of what we stand to lose. Portions of
BCT-TPORT were co-invented with **Nic**, housemate and best friend.

🦜
