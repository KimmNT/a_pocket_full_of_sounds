# APFS project instructions

This project is A Pocket Full of Sounds (APFS), a browser game with pastel 2D cartoon art, chibi characters, and soft music, intended for low-spec laptops and PCs.

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

The game is at the design stage with five selected game concepts: Blow the Candle, Press to Find Matching Sounds, revised Pepper Soup (exact-order cooking for a starving monster), The Backwards Vacuum, and The Shell Game. The first five are confirmed in that listed encounter order. The user requested two remaining guardian ideas plus a final-boss game. Section 16 is the dedicated workspace for scenes and individual monster stories. Section 8 proposes The Crumbling Maze, The Ink Painter, and The Storm Engine finale; these three are unselected. Mirror Garden, Balance the Hoard, and earlier musical ideas are parked. Follow the user's current request; do not treat new proposals as approved or start full implementation from planning alone.

## Essential constraints

- Maintain low-spec performance as a design goal; measure it before claiming success.
- There are seven unique natural-note energies and each note guardian owns exactly one, with sharp-note stock otherwise. Do not create extra natural-note resources for puzzles. Prefer the user's current request for non-musical challenges; soundtrack music and note-recovery rewards remain.
- When natural notes are stolen, the lantern stops illuminating the world and instruments are left with sharp notes. Do not assume instruments can reproduce missing natural pitches. The historical multi-natural-note password needs revision; keep the established lock and flag unavailable-white-key behavior and the restoration timing of recovered pitches as OPEN.
- No repeated playable returns home. Each absorbed airy note grants one tunnel charge then goes straight to the lantern; it does not stay inside the character. Each encounter has a predefined entry and successful tunnel escape scene. Entry is not confirmed to use the tunnel or a charge; no free destination choice or unlimited stored-note recharge.
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
- Pocket tunnel uses the one earned charge for the fixed encounter escape. Exact staging and final activation input remain OPEN. Do not restore automatic shelf pickup on audition.
- Failure restarts the entire current encounter, including all stages, without intermediate-stage checkpoints; earlier completed encounters are not replayed. Keep games straightforward. Warn before danger/irreversible outcomes, including the Shell Game third return, which catches the player even when hidden.
- Minimize web animation code. The Vacuum wake-up button starts a noninteractive character-to-column-to-monster-knockout sequence. A short clip or simple authored animation is acceptable; prefer simple optimized animation when practical, with no chosen format or measured performance yet.
- Revised cooking: scary cave entrance-to-throne; starving monster lying at the end; eight available ingredients; exact preparation order. Wrong order still produces a meal and kills the monster when eaten, making its internally held note disappear. Correct meal saves it; it voluntarily gives the note and says the final boss threatened its family. Do not restore the superseded pepper/sneeze/belt-trap plot or silently soften the failure into sleep. Recipe clues remain OPEN; failure restarts the whole cooking encounter, restoring the monster and note for the new attempt.
- The final boss is the Monster King, the world's most powerful monster. All seven guardians serve under threat of death, but some also respect him and some are good monsters forced to steal. Only the cooking guardian has the specific family-threat story assigned. Individual loyalties and army motives remain OPEN. The final battle has no eighth natural note; proposed finale phases and ally participation remain unapproved.
