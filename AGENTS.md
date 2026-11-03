# APFS project instructions

This project is A Pocket Full of Sounds (APFS), a browser game with doodle art and soft music, intended for low-spec laptops and PCs.

## Read before continuing

Read `GAME_DESIGN.md` in full before making design or implementation decisions. It records confirmed requirements, proposals, open questions, progress, and the next work. The user's latest instructions take precedence.

## Keep documentation current

The user explicitly requests two maintained documents:

- `A Pocket Full of Sounds - Game Design.html`: readable human design document.
- `GAME_DESIGN.md`: portable AI handoff and canonical design source.

After every material design decision or implementation milestone, update both documents with the same version and date. Keep their factual content synchronized. Preserve the distinction between confirmed requirements and suggestions. Record what actually exists and what has been tested. Never imply that a planned feature is implemented.

Edit the Markdown first, then run `python build_docs.py` from the project folder to regenerate the HTML. The helper uses only Python's standard library, retains the existing HTML style, and embeds the Markdown source hash. If Python is unavailable, update the HTML directly to match. Regenerate only after reconciling any separate user edits to the HTML.

Keep the files together in the project root, currently `C:\Users\JoseKim\Desktop\APFS`. If moved, update the documented path. Preserve and reconcile user edits before replacing files. Copies exported to other locations are snapshots. No automatic background synchronization has been configured.

## Current work

The game is at the design stage with five selected game concepts: Blow the Candle, Press to Find Matching Sounds, revised Pepper Soup (exact-order cooking for a starving monster), The Backwards Vacuum, and The Shell Game. The user approved the last three on 2026-10-23 and requested two remaining guardian ideas plus a final-boss game. Section 8 proposes The Crumbling Maze, The Ink Painter, and The Storm Engine finale; these three are unselected. Mirror Garden, Balance the Hoard, and earlier musical ideas are parked. Follow the user's current request; do not treat new proposals as approved or start full implementation from planning alone.

## Essential constraints

- Maintain low-spec performance as a design goal; measure it before claiming success.
- There are seven unique natural-note energies and each note guardian owns exactly one, with sharp-note stock otherwise. Do not create extra natural-note resources for puzzles. Prefer the user's current request for non-musical challenges; soundtrack music and note-recovery rewards remain.
- The ordinary instrument-pitch versus unique note-energy distinction is OPEN. Flag the existing multi-natural-note example password for lore review instead of silently deleting the established lock or inventing a rule that reproducing pitches creates additional notes.
- No repeated playable returns home between encounters; note absorption restores the village lantern remotely.
- Right-click a walkable surface to move; left-click to interact.
- Microphone input estimates blowing strength; the game plays its own authored blowing effect. Do not play back raw microphone audio.
- Microphone reliability and all detailed candle timing remain untested.
- The melody demonstration plays sounds and displays note names. The lock itself has seven white keys and five black keys, without labels. Do not add automatic key-position hints or labels without user direction.
- The first lock keypress starts the countdown regardless of correctness. Correct next notes get positive color feedback; a wrong note clears all entered progress. Treat that as an input reset rather than a timer reset, with final timing validation still open.
- Basement shelf: four columns by three rows, twelve slots holding exactly six randomly placed objects (five sharp-note decoys and one natural target). Player must move to a column to audition its notes. Preserve selected-note names on audition.
- Notes are airy forms trapped through a sucking ability/device provided by the final boss; the exact tool and art treatment remain open.
- Clicking a shelf note auditions it and shows its name; it no longer automatically collects the natural target.
- ABSORB/COLLECT is a separate button: the character takes out the pocket tunnel and reveals an area. A natural note inside pops/disappears, is absorbed, and grants a tunnel escape use. No natural note inside produces a comic empty reaction.
- Repeated failed absorption makes the character angry and sleep for five seconds. Failure threshold, reset rules, exact disabled inputs, and danger-timer behavior during sleep remain open. Count only failed absorption actions, not ordinary note auditions.
- Pocket tunnel uses natural-note power. Its destination, general recharge restrictions, and automatic versus manual use of the earned escape remain open. Do not silently restore the superseded automatic pickup-on-click rule.
- Revised cooking: scary cave entrance-to-throne; starving monster lying at the end; eight available ingredients; exact preparation order. Wrong order still produces a meal and kills the monster when eaten, making its internally held note disappear. Correct meal saves it; it voluntarily gives the note and says the final boss threatened its family. Do not restore the superseded pepper/sneeze/belt-trap plot or silently soften the failure into sleep. Recipe clues and retry/checkpoint versus a permanent failed ending remain open/proposed.
- The cooking monster's coercion is confirmed for that monster only. Do not assume all guardians or the army have the same motive. The final battle has no eighth natural note; all proposed finale phases and ally participation remain unapproved.
