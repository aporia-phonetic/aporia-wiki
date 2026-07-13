# Caelum Reach

`world_id`: `caelum_reach`

Caelum Reach sits on a wide river bend — the Acheron Cut, locals call it, though the name predates living memory — in a world that has just discovered electricity and hasn't decided what to do about it yet. The city proper sprawls across both banks, connected by three iron bridges and one wooden one that nobody trusts. Coal smoke and river fog are permanent features of the skyline. The architecture is dense, ornate, and slightly wrong — built over centuries by hands that weren't entirely mortal, with columns that go a touch too tall and archways that curve at angles that make surveyors uncomfortable. It looks like Chicago if Chicago had been designed by people who remembered building temples. It runs on coal, electric cable lines, animal labor, and increasingly on magical infrastructure that nobody has formally named yet.

The city is governed — in the way a watershed is governed by the largest rock in the river. Zeus holds the office of Mayor, appointed himself to it some decades ago, and has retained it through a combination of genuine charisma, strategic lightning, and ballot boxes that do not always behave. Hades operates the organized criminal apparatus from the lower city, the waterfront warehouses, and the tunnels beneath the old district that the city maps don't show. Poseidon controls the docks, the port authority, the river pilot guilds, and every loan that has anything to do with moving goods across water — which is to say, most loans. These three do not cooperate. They do not need to. They carved the city into thirds before anyone currently living was born and the arrangement has held because none of them want the war that overturning it would require. The rest of the Pantheon fills in the civic and commercial structures beneath: Athena runs the police department, Hermes runs the largest shipping conglomerate on the continent, Hephaestus owns the foundries and the electrical grid, Ares controls the city's private security firms and what remains of the standing militia. Aphrodite's holdings in hospitality and entertainment are vast and deliberately unmapped. Apollo runs a newspaper. Artemis runs a detective agency, or funds one, or is one — it depends who you ask and when. The gods are not in hiding. They are in *charge*. They simply do not announce what they are.

The city is wealthy, crooked, and functional the way a machine is functional — it does what it does, it does not care what it costs the components. Mortals fill every stratum of the city's life. They run the banks, drive the cabs, work the docks, play the music, print the papers, and occasionally find themselves in possession of something — information, a debt marker, a body — that the divine machinery has misplaced. When that happens, things get interesting. The gods, broadly, do not consider individual mortals significant. This is not cruelty so much as *scale*. The gods move in centuries; a mortal life is a short candle. The exception — the crack in the doctrine — is that a mortal who *proves themselves* shifts category. A mortal who matters gets noticed. The gods will never say this plainly. They don't have to. The whole city is organized around the unspoken contest to become someone who matters.

Technology is in genuine transition. Trains are infrastructure; they have been for fifty years. Personal ground automobiles are appearing — some petrol-driven, some electrically cabled for use within city districts, a few that run on divine-adjacent mechanical systems that nobody has properly certified. A small number of airships make regular port at the elevated dock on the river's north bluff. Technomancy — the discipline of fusing intentional magical practice with emerging electrical and mechanical systems — is beginning to manifest in the population. It has no formal name yet. The people developing it mostly don't know what they are doing. The gods are watching this development with an interest they are careful not to display.

---

## Primary Locations
| Location Name | Description | Reverb Profile | Initial Status |
|---|---|---|---|
| The Olympian — City Hall & Mayor's Offices | A twelve-story stone tower with ionic columns that are about four feet too wide, overlooking the central plaza; Zeus's offices occupy the top two floors, and the building has a habit of throwing off small static charges when the Mayor is in residence. | `grand_atrium` | `established` |
| The Acheron Cut (Waterfront District) | Poseidon's jurisdiction — the two-mile stretch of working docks, port authority warehouses, import brokerages, and sea-salted bars where the river pilots drink before and after they shouldn't; always smells of coal oil, fish, and the particular cold that comes off moving water. | `eastern_passage` | `established` |
| The Lower City (Hades' Quarter) | The original city footprint, partially underground by design and partially by subsidence, where the streets are narrower than the maps show and the electric lights are fewer and more amber; Hades' legitimate offices front a funeral services conglomerate that occupies an entire block. | `camp_1` | `established` |
| The Precinct — Athena's Metropolitan Police HQ | A wide granite building two blocks from City Hall with an owl worked into the cornerstone; Athena runs it with the precision of someone who has read every relevant text on civic order and written several of them, and the detectives here are the best-trained in the country — and watched accordingly. | `grand_atrium` | `established` |
| The Bacchanal — Bacchus's Nightclub | Three floors of the best music in the city, a bar that is never fully stocked because it is never fully unstocked, and a private membership tier that nobody can explain the criteria for; Bacchus is present most nights in one form or another, and the club has a documented ability to make people forget what time it is. | `default` | `established` |
| Hermes Consolidated Shipping (The Waypoint Building) | A glass-and-steel commercial tower near the rail terminus with the winged-post logo on every surface; the largest shipping brokerage on the continent and also, not coincidentally, the fastest information network in the city — what moves through Hermes's manifest system moves everywhere eventually. | `eastern_passage` | `established` |
| The Bluff Aerodock | An elevated platform on the river's north bluff, accessible by a cable-car lift from street level, where the city's small fleet of commercial airships make berth; less regulated than the river docks because Poseidon's authority ends at the waterline and Zeus hasn't yet decided whether to contest the airspace. | `default` | `established` |
| The Foundry Grid (Hephaestus District) | The industrial east quarter where the electrical generating stations and heavy foundries operate around the clock; technomancers have discovered that this district carries the strongest ambient resonance in the city, and a small, mostly unaware community of them has grown up in the boarding houses nearby. | `camp_1` | `established` |

---

## Starting Resources
| Resource | Starting Amount | Unit | Notes |
|---|---|---|---|
| Currency | Moderate | city marks | The city runs on the Reach Mark; the gods deal in older currencies when they deal directly |
| Fuel (Coal/Petrol) | Plentiful | — | Infrastructure resource; scarcity only matters if someone is controlling supply deliberately |
| Information | Scarce | — | The city has three newspapers, two of which are compromised and one of which (Apollo's) is accurate in ways that are sometimes inconvenient |
| Divine Favor | Depleted | — | PCs begin with no established relationship with any deity; earning one is a season-long arc |
| Transportation | Limited | — | Rail is public; personal automobiles are expensive; airship passage is available but logged by Hermes's people |

---

## World-Specific Tracked Variables
- `divine_attention_zeus: 0` — How much the Mayor's office is aware of protagonist actions. Increases when characters operate in civic, electoral, or legal domains. At 75+, Zeus takes personal notice.
- `divine_attention_hades: 0` — How much the underworld organization is tracking the protagonists. Increases with lower-city activity, criminal interference, or contact with the dead. At 75+, Hades extends an invitation. Invitations from Hades are not optional.
- `divine_attention_poseidon: 0` — Port authority and docks surveillance. Increases with waterfront activity, shipping interference, or unauthorized river transit. At 75+, harbor agents become actively hostile.
- `pantheon_tension: 35` — Baseline friction between the three ruling powers. Increases when protagonists disturb the existing balance. At 60+, proxy conflicts begin manifesting visibly in the city. At 90+, the truce structure is under active strain.
- `technomancy_exposure: low` — How visible the emerging technomancer community is to divine awareness. Currently below the threshold of concern. Increases as characters engage this community or use technomantic methods publicly.
- `mortal_credibility: 0` — The gods' private assessment of whether the protagonists have begun to *matter*. Cannot be tracked directly; manifests as changed behavior from divine-tier NPCs when it crosses thresholds.

---

## Forbidden Tropes
- The gods are never stupid. They are arrogant, bored, distracted, or politically constrained — not foolish. If a mortal outmaneuvers a god, it cost the mortal something significant.
- No "chosen one" framing. Mortals earn significance through action and consequence, not destiny.
- The divine is never merely colorful background. Every god present has an agenda. Every agenda has implications.
- Magic is not a clean solution. Divine power invoked always costs more than the invoice shows.
- Noir cynicism is the *start*, not the conclusion. Characters who believe nothing matters are wrong — the story exists to prove it.
- The city is not secretly good underneath it all. It is actually corrupt, actually wealthy, and the corruption actually benefits some people. Reform is real but expensive.
- No comedy sidekick. Every recurring character, however small, carries weight.
- Demigods are not automatically heroic. Divine lineage is a condition, not a character.

---

## Series Bible Summary
### THE PANTHEON IN RESIDENCE — Known Holdings & Positions

**Zeus** — Mayor of Caelum Reach. Has held the office through four contested elections. His mortal-presenting form is a large, well-dressed man in his apparent late fifties with white hair and the kind of handshake that feels like a warning. His office on the twelfth floor of the Olympian is rumored to have a view that changes depending on his mood. He is charming, politically astute, and has a documented inability to leave attractive mortals alone that has created more than one political liability.

**Hades** — Operates under the name Mr. Pluto in the city's mortal-facing paperwork. Runs a funeral conglomerate (Pluto & Associates, Est. before living memory) that is the city's largest legitimate business by revenue, and an underworld criminal apparatus that is the city's largest illegitimate one. He is quiet, immaculately dressed, and the only member of the Pantheon whom Zeus does not attempt to outmaneuver directly. He keeps a three-headed dog. People have learned not to ask about it.

**Poseidon** — Goes by Captain Pelagic in dock circles, no last name, which everyone accepts because challenging a harbor master the size of a door and the temperament of a storm front is not a profitable activity. The port authority answers to him absolutely. He is the only member of the Pantheon who still spends significant time in his natural form — usually on the water, usually at night, visible only to those who are already in some trouble.

**Athena** — Chief of Police, known as Commissioner A. Metis in official documents. Runs the Precinct with the precision of someone who has memorized every law in the jurisdiction and is quietly disappointed by how few other people have. She is the most politically legible of the Pantheon — transparent in her standards, consistent in her enforcement, which makes her simultaneously the most trustworthy and the most dangerous, because her version of justice does not bend for relationship. She has an owl that lives in the Precinct rafters. Rookies learn not to report it.

**Hermes** — CEO of Hermes Consolidated Shipping. Goes by Henry Merk in mortal business contexts. The fastest mind in the room in every room, which means he is usually several meetings ahead of whatever meeting is currently occurring. His shipping network is legitimate; his information network is not something he acknowledges; his role as the Pantheon's internal messenger is something only the other gods are fully aware of.

**Hephaestus** — Owns the foundries and electrical generating infrastructure of the Foundry Grid district. Never appears in public. Communicates through a series of foremen and mechanical intermediaries. Brilliant, reclusive, embittered. The electrical grid of Caelum Reach runs better than any comparable city's because he designed it and remains invested in it — but accessing him requires navigating the intermediaries, and the intermediaries are strange.

**Bacchus** — Proprietor of The Bacchanal. No last name used, no official mortal alias, which somehow never causes legal problems. Present most nights. Knows everyone's name after the first drink and their deepest want after the second. The club's private membership tier — access to the third floor — is the city's most coveted and least understood social currency. What happens on the third floor does not stay on the third floor in any simple sense; it tends to reshape whoever was there.

**Apollo** — Publisher and lead columnist of *The Reach Standard*, the city's only reliably accurate newspaper. Goes by A.P. Solaris in print, which everyone sees through and nobody challenges because his lawyers are excellent and his evidence is always ironclad. He is the Pantheon member most engaged with mortal life as a genuine interest rather than an administrative matter, and the one most likely to publish something inconvenient to Zeus, which Zeus tolerates with visible effort.

**Artemis** — Operates in the city in several overlapping capacities that she does not consolidate into a single identity. She is known to fund at least one private detective agency, to run a network of contacts across the less-charted districts, and to appear at significant moments in cases involving violence against those who cannot protect themselves. She does not have a listed address. She is not difficult to find if something has gone genuinely wrong.

**Aphrodite** — Her holdings in hospitality, entertainment, and what the city's accounting euphemistically terms "relationship services" are the widest footprint of any Pantheon member except Hades. She does not run these operations from a central location. She is present in them the way water is present in a building — through every wall if you know where to look. Her mortal-presenting form changes depending on who is looking at her, which is not metaphor.

**Ares** — Controls Reach Security Solutions, the largest private security and enforcement firm in the city, and maintains informal relationships with every militia fragment and veterans' organization in the region. He is the Pantheon member most visibly involved in physical conflict and the one least interested in its political context. He has strong feelings about this, which he expresses by breaking things.

---

### THE TECHNOMANCER COMMUNITY

No formal organization. No acknowledged existence. A loose scatter of engineers, mechanics, electricians, and the occasional academic who has noticed that machines behave differently in certain locations at certain times, and that the behavior is learnable. They meet informally in the boarding houses near the Foundry Grid and in the back room of an electrical supply shop on Copper Lane. They do not have a name for what they do. They are beginning to look for one. The gods are aware this is happening. No one has yet decided what to do about it.

---

### THE DEMIGOD POPULATION

Spread throughout the city, mostly unaware of each other. Some know what they are; many don't. The ones who know tend to have survived something that required them to find out. They move in mortal life — working jobs, running businesses, making lives — with a private knowledge that they are not entirely what the people around them think they are. They age slowly enough that they have to move periodically to avoid notice. They are not a community. They are a shared condition.

---

### THE THREE-POWER TRUCE

The arrangement between Zeus, Hades, and Poseidon is not written down anywhere. It does not need to be. The broad strokes: Zeus holds civic authority and public face. Hades controls underground commerce and the dead. Poseidon controls the water and everything that moves on it. Each stays out of the others' territory in matters of direct power. Each exploits the edges of everyone else's territory in matters of indirect influence. The truce has held for longer than the city has existed in its current form. It will not hold forever. The thing most likely to destabilize it is not mortal action — it is one of the three deciding that an advantage is finally worth the war. Protagonists who stumble into the edges of this arrangement will be used. The question is whether they can use it back.

---

### TRANSPORTATION NOTES

- **Rail:** The Caelum Reach Central Terminal connects the city to the broader continent. Trains run four lines. Reliable, public, monitored by Hermes's freight operation.
- **Cable cars:** District-specific electric tram lines run within the dense city blocks. Hephaestus's grid. Cheap, slow, always crowded.
- **Personal automobiles:** Expensive and increasingly visible among the wealthy. Some petrol. Some cabled (usable only within districts with the infrastructure). A few that operate on systems their owners cannot explain and that mechanics cannot fully service.
- **Airships:** Three commercial lines make regular port at the Bluff Aerodock. Expensive. Not regulated by the port authority (Poseidon's jurisdiction ends at water level). The regulatory gap is noticed and not yet filled.
- **River transit:** Ferries cross the Acheron Cut. Pilot boats, freight barges, and what the port authority calls "informal river commerce" (everyone else calls smuggling) move on the water. All of it answers to Poseidon.

---

## Season Premise
Someone has died in Caelum Reach in a way that should have been impossible — a death that crossed all three divine territories simultaneously and left no thread that any of the three powers can pull without implicating themselves. The question is not who did it. The question is *what was the victim carrying* that made the impossible happen, and whether there is more of it, and who else knows. The dramatic question underneath: in a city owned entirely by beings who do not consider mortals significant, what does it cost a mortal to find out something the gods collectively don't want found?

---

## Season Arc
The world begins in a stable, ruthless equilibrium — three divine powers controlling a wealthy city, mortals filling the machine, the system crooked but functional. By the final episode, something has been introduced into the city that none of the three powers anticipated, the truce structure has been tested at a load it wasn't designed to carry, and at least one mortal has crossed the threshold from *person* to *someone who matters* — with all the danger that entails.

---

## Genre & tone

- **Genre:** noir
- Chinatown* — the system is the villain, corruption is structural, and winning looks like surviving with something still intact.
- The feeling of a building that used to be a temple and now houses a shipping office. The columns are still there. Nobody mentions them.
- Raymond Chandler prose in a world where the dame at the end of the bar is actually the goddess of love and she is not here for the ambiance.
- Coal smoke and ozone. The smell of a city that runs on something it doesn't fully understand.
- The moment a mortal realizes the god they've been dealing with has been paying attention to them specifically, and for longer than they knew.

## Status

- Seasons: [season_01](../seasons/caelum_reach/season_01.md)
- Full sourcebook: `heterodyne/data/worlds/caelum_reach/sourcebook.md` (not mirrored here — see that file in the engine repo for the complete series bible)
