# A Pocket Full of Sounds

## Project record

- Project abbreviation: APFS.
- Version: 0.19.
- Updated: 2026-11-10 (Asia/Bangkok).
- Project folder: `C:\Users\JoseKim\Desktop\APFS`.
- Stage: story and gameplay design; no game implementation or performance testing yet.
- Human document: `A Pocket Full of Sounds - Game Design.html`.
- AI handoff and canonical design source: `GAME_DESIGN.md` (this file).
- Persistent project instructions: `AGENTS.md`.
- HTML refresh helper: `build_docs.py` (Python standard library only).

This is a portable record of the conversation. Another AI should read the whole document before continuing. Use ordinary, precise language; no special AI-only language is necessary. The HTML and Markdown must describe the same current design and carry the same version.

## Status definitions

- CONFIRMED: chosen or specified by the user.
- PROPOSED: suggested during discussion; not a final requirement.
- OPEN: needs a decision or validation.
- SUPERSEDED: an earlier direction that no longer applies.

Do not convert a proposal into a confirmed requirement merely because it appears in this document. New user instructions take precedence.

## 1. Confirmed game direction

- Browser-based game for low-spec laptops and PCs.
- 2D cartoon art with chibi characters and pastel colors; soft songs remain part of the direction.
- Sound is part of the world's life and energy.
- Eight play rounds: seven note-recovery mini-games and one final battle.
- Each note guardian has its own battle style.
- Confirmed order: 1 Blow the Candle; 2 Press to Find Matching Sounds; 3 The Starving Monster's Meal (revised Pepper Soup); 4 The Backwards Vacuum; 5 The Shell Game. Guardians 6 and 7 and final-battle mechanics remain unselected.
- Failure restarts the current encounter from its beginning, including all stages, without intermediate checkpoints. Keep games straightforward and give warnings before dangerous or irreversible consequences.
- There are only seven unique natural-note energies. Each of the seven note guardians holds one; its other note stock consists of sharp notes. Do not introduce extra recoverable natural notes for a mini-game.
- Latest ideation preference: suggest non-musical challenges. Musical atmosphere and natural-note recovery remain part of the world, but the remaining games do not have to test songs, sound, note names, or melody.
- Maintain tension through an outward journey. Do not require repeated playable returns to the village between rounds.
- The user will supply boss ideas individually. Review feasibility, technical approach, low-spec performance, gameplay fairness, edge cases, and possible adjustments.

## 2. Story

### CONFIRMED narrative

The village lives on sound. Seven unique natural notes energize its life. Each of seven note-holding monsters possesses one stolen natural note; its other note stock consists of sharp notes. The eighth monster is the final-battle boss, not the holder of an additional eighth natural note.

On a night of heavy rain, eight monsters steal all seven notes. The lantern stops illuminating the world because its seven natural notes are missing. Instruments are left with sharp notes; they cannot freely reproduce the stolen natural pitches. A further threat is approaching, capable of taking the world down.

Our character sets out to recover the notes. Each of the first seven rounds is a mini-game whose victory recovers one note. The village gradually regains its sound and light.

After all seven notes are recovered, the village celebrates. Gray clouds cover the sun, heavy rain returns, and the eighth boss arrives with its entire army. Round eight is the final battle.

The final boss is the Monster King, the most powerful monster in the world. All seven guardians serve him under threat of death for refusing his service. Personal loyalties differ: some also respect him, while some are good monsters forced to steal. Specific assignments remain OPEN except for the starving guardian, whose family was threatened. Saving that monster earns its voluntary note gift and reveals this coercion. Do not assume all guardians are unwilling or that the army shares one motive.

### PROPOSED narrative details

- Develop the individual guardian stories in section 16. The king's authority and mixed loyalties are confirmed, but new individual backstories are not yet chosen.
- Pip is a suggested protagonist name, not a confirmed name.
- The final battle could combine actions learned in the earlier encounters.

### OPEN narrative details

- Protagonist identity, appearance, and final name.
- Monster names, individual loyalty/coercion assignments beyond the starving guardian, the king's theft motive, and army motives.
- Location of the final battle and whether the character returns home once at the end.
- How the army is represented and what happens after victory.
- Reward pitches for encounters 2-7 and exact naming scheme. Order 1-5 is confirmed; C remains the candle reward.
- Instruments lose the stolen natural pitches and retain sharp notes. The confirmed all-sharp password resolves the earlier basement melody conflict. Unavailable-white-key behavior and which recovered natural pitches return to instruments, and when, remain OPEN; do not assume unrestricted reproduction or extra natural-note resources.

## 3. Notes and village lantern

### CONFIRMED note form and capture concept

- Notes exist as airy, intangible forms rather than ordinary solid objects.
- Monsters can suck natural notes into a containing ability or device supplied by the final boss. Whether this is an innate/granted ability or a physical tool is not finalized.
- This gives the stolen notes a visible trapped form that can be shown on screen and recovered.

PROPOSED visual treatment: simple translucent cartoon wisps or air swirls confined within small visible traps on the shelf. Containers, colors, outlines, and note-symbol decorations are not finalized. Do not reveal which untested wisp is natural through a unique visual treatment unless deliberately chosen.

### CONFIRMED system

- The character can absorb recovered notes.
- A lantern at the village has seven note slots.
- Absorbing an airy note grants one pocket-tunnel charge, then sends the note directly to its lantern slot and restores it. The note does not stay in the character.
- The village recovers without the character traveling back and forth.

### CONFIRMED pocket tunnel ability

- The character has a pocket tunnel in addition to note absorption.
- Only the power of a natural note can activate the tunnel.
- The character takes out the pocket tunnel when the player presses an ABSORB or COLLECT button. It reveals a defined absorption area.
- A natural note inside that area is absorbed with a pop/disappearance, granting an escape use of the pocket tunnel.
- If no natural note is inside the area, the character performs an empty-absorption reaction.
- Repeated unsuccessful use makes the character angry and then sleep for five seconds, as a comic consequence. Exact trigger count and reset rules remain OPEN.
- Sharp-note decoys do not activate the tunnel.

CONFIRMED: each newly absorbed natural note grants one tunnel charge and then travels straight to the lantern. Spend that charge on the encounter's predefined escape scene; recovered notes are not stored as reusable escape batteries. Entry into each monster's place also uses a predefined scene. This is a simple transition system, not free destination selection. Entry scenes are not confirmed to use the tunnel or require a charge. Exact entry/exit staging and whether one final activation input starts the escape scene remain OPEN.

### PROPOSED explanation and presentation

- A visible trail could show the confirmed direct transfer of the note to the lantern after granting a tunnel charge; exact visuals are proposed.
- A brief glow could signal the single charge; permanent stored-note marks are not confirmed.
- Short, wordless village scenes show one lantern chamber lighting and something recovering.
- Each recovered note adds a musical layer to the soundtrack.
- Additional note-specific abilities remain optional. Absorption and the natural-note-powered pocket tunnel are confirmed, but there is no established wider ability progression system.

## 4. Confirmed controls and blowing behavior

| Input | Intended behavior | Status |
| --- | --- | --- |
| Right-click a walkable surface | Character moves toward the clicked destination | CONFIRMED |
| Left-click | Interact with objects or characters | CONFIRMED |
| ABSORB or COLLECT button | Take out pocket tunnel and check its visible absorption zone for a natural note | CONFIRMED mechanic; final label and zone rules open |
| Blow into microphone | Microphone estimates blowing strength for the in-game gust | CONFIRMED direction; not implemented |
| Game's authored sound effect | Play our designed blowing sound rather than raw microphone audio | CONFIRMED |

Microphone input and game audio output are separate:

`Player breath -> local microphone analysis -> calibrated strength -> character gust + authored blowing sound`

Microphone loudness is an estimate of breath strength, not a direct measurement of air pressure. Distance, gain, and microphone sensitivity affect readings.

### PROPOSED control details

- Show a destination marker and reject unreachable destinations.
- Keep movement within valid walkable areas.
- Suppress the browser context menu inside the play area; test browser exceptions.
- Define interaction range so clicking a distant object does not unexpectedly walk the character into danger.
- Provide an alternate on-screen or keyboard blowing control when microphone use is unavailable or unsuitable.

### OPEN control details

- How to stop or cancel movement.
- Whether blowing pauses movement and clears or preserves the destination.
- Whether distant interactions are rejected or queue movement.
- Exact fallback input and whether microphone mode is optional in the final game.
- Final absorption-button label, zone size/shape/aim, and whether a separate ESCAPE press uses the earned tunnel charge.

## 5. Encounter tracker

| Encounter | Reward | Current status |
| --- | --- | --- |
| 1. Blow the Candle | Note C | First encounter confirmed; tuning open |
| 2. Press to Find Matching Sounds | Natural note, pitch not assigned | Countdown piano lock; randomized shelf search; area-based ABSORB/COLLECT; earned tunnel escape; repeated empty attempts cause a five-second sleep; no chase |
| 3. Pepper Soup - revised starving-monster meal | Natural note, pitch not assigned | CONFIRMED user revision: eight ingredients, exact cooking order, lethal wrong meal, compassionate success, family-coercion reveal |
| 4. The Backwards Vacuum | Natural note, pitch not assigned | Three stacked puzzles conceal a reverse switch; sleeping monster; wake-up button scripts a column falling straight onto its head; monster activates reversed machine; overloaded ejection recoils it into the wall, knocking it unconscious; absorption animation and tunnel escape |
| 5. The Shell Game | Natural note, pitch not assigned | Three-shell mixing machine; observe the shuffle; wrong choice triggers an ambulance-like alarm; first two returns: attitude, search, and note reset while player hides; third return: guaranteed capture even when hidden |
| Guardian slot 6 | Sixth natural note, pitch not assigned | The Crumbling Maze proposed; not selected |
| Guardian slot 7 | Seventh natural note, pitch not assigned | The Ink Painter proposed; not selected |
| Final boss and army, round 8 | Defend the recovered world; no eighth note | The Storm Engine proposed as a three-phase finale; not selected |

Five encounter concepts are selected in confirmed order: 1 Blow the Candle, 2 Press to Find Matching Sounds, 3 The Starving Monster's Meal (revised Pepper Soup), 4 The Backwards Vacuum, and 5 The Shell Game. Reward assignments except candle C and detailed tuning remain OPEN. Two guardians and final-battle mechanics still need selection; The Crumbling Maze, The Ink Painter, and The Storm Engine remain proposals.

On 2026-10-23 the user requested non-musical alternatives, approved The Backwards Vacuum and The Shell Game, and replaced the pepper/sneeze premise with an eight-ingredient meal for a starving monster. Section 8 records these accepted concepts, two new guardian proposals, a proposed finale, and parked alternatives. Do not count parked ideas as extra rounds.

## 6. Blow the Candle

### CONFIRMED encounter concept

The character is in a cave. A huge candle at its center provides the light. The boss faces a wall and does not see the character directly. When the character walks in, their shadow appears on the wall the boss watches.

The player must blow out the candle before moving toward note C. The boss repeatedly relights the candle. The player must extinguish it quickly enough to avoid being noticed, continuing until the note is reached and taken.

The microphone estimates the player's blowing strength. The game's own blowing sound plays for the character's gust; raw microphone input is not played back.

### Feasibility assessment

Suitable for a lightweight 2D browser implementation. Use a cave background, character, boss, candle, and a stretched dark silhouette for the wall shadow. Realistic lighting simulation is unnecessary. This is an architectural assessment, not measured performance.

### PROPOSED playable loop

1. Explain the shadow from a safe entrance.
2. Player blows out the candle and advances.
3. Boss gives a visible relighting warning.
4. When the candle lights, the shadow appears and suspicion rises.
5. Player extinguishes the candle before suspicion fills.
6. Reaching and absorbing note C immediately completes the encounter.

### Edge cases and PROPOSED adjustments

| Risk | Proposed handling |
| --- | --- |
| Character moves too far away to blow naturally | Establish a visible ranged puff of wind and explain its reach |
| Continuous blowing or fan noise keeps the candle out | One puff per accepted breath, a recovery interval, and a quiet reset before rearming |
| Repeated puffs while walking bypass timing | Test a brief movement interruption and recovery for unnecessary early puffs |
| Standing still incorrectly hides the character | Detect shadow exposure, including while stationary |
| Darkness makes navigation unreadable | Keep faint scenery outlines and a glowing note; distinguish ambient visibility from dangerous candlelight |
| Candle relights and causes instant failure | Provide a warning and reaction allowance; around one second was an initial test suggestion only |
| Shadow geometry contradicts the room layout | Keep the route between the candle and the wall watched by the boss |
| Boss turns around to relight | Boss sends a spark without looking away from the wall |
| Minor mistakes require excessive retries | Test suspicion that rises in light and gradually falls in darkness; failure rules remain open |
| Player changes browser tab | Pause on focus loss; base timers on elapsed time, not rendered frame counts |
| Note absorption and detection occur together | Commit successful absorption before another detection event can cause failure |

All adjustments above are proposals unless the user explicitly finalizes them. Exact relighting cadence, suspicion behavior, detection window, and failure presentation are OPEN. Failure restarts the entire candle encounter.

## 7. Press to Find Matching Sounds

### CONFIRMED encounter concept

A monster keeps a stolen natural note in its basement. The character watches the monster leave the basement and play a melody to lock it. Each played note is heard and its name is displayed. CONFIRMED password for encounter 2: `C#, F#, G#, D#, A#, A#` (C? ? F? ? G? ? D? ? A? ? A?). This is a fixed six-note sequence selected by the user. It replaces the historical example `C, D#, G, A#, B, B`.

CONFIRMED lore: instruments lose stolen natural pitches, leaving sharp notes. The chosen password uses only sharp notes and needs no unavailable natural pitch. Keep the named demonstration and unlabeled twelve-key lock. Unavailable-white-key behavior remains OPEN, including whether recovered C becomes available by encounter 2. Do not silently remove keys, add labels, fabricate missing pitches, or assume the guardian can play other stolen natural notes.

The final two A# notes require two separate keypresses; holding the key does not enter both. Octave/register, rhythm requirement, playback pacing, replay behavior, and countdown duration remain OPEN. Keep all twelve unlabeled keys; selecting this melody does not add key-position hints.

After the monster leaves, the character can approach the door and click its lock without alerting the monster. The lock opens a piano-style keyboard with seven white keys and five black keys. The lock has no note-name labels. The player must reproduce the remembered melody on that unlabeled keyboard using the sounds, shown names from the demonstration, and their knowledge or discovery of key positions.

There is no playable chase. The first player keypress alerts the monster and starts a countdown, whether the note is correct or wrong. When time expires, the player is caught.

Correct notes in the correct order receive green or another clear success color. A wrong note erases the entire entered sequence and its progress feedback, requiring the player to begin that sequence again. The encounter is timed from the first note: interpret sequence erasure as resetting input progress, not resetting or restarting the countdown. This timer continuity is an implementation reading of the user's rule, rather than a separately chosen timing mechanic.

A completed melody opens the door. The character jumps into the basement and the door locks behind them. The monster then tries to break through while a basement time limit pressures the search.

The basement shelf has four columns and three rows: twelve slots, not twelve note objects. Six notes occupy six randomly chosen slots: five sharp-note decoys and one correct natural note. The remaining six slots are empty.

The character must move to a column to play the notes in that column, then move to another column to inspect its notes. Clicking a note plays its sound and shows its name. It no longer automatically collects the target.

The notes are airy forms trapped by the monster's sucking ability or a device supplied by the final boss. The player presses an ABSORB or COLLECT button; the character takes out the pocket tunnel and reveals a particular absorption area. If the natural note is inside, it pops/disappears into the tunnel and the character gains a tunnel escape use. If the target is outside the area or no natural note is present, the character reacts that there is nothing to absorb. Repeating unsuccessful absorptions makes the character angry and then fall asleep for five seconds. The user wants this to be funny.

The area-based button mechanic supersedes the earlier automatic collection on note click. Escape uses the predefined scene; whether it starts immediately after absorption or after one final activation remains OPEN.

The intended target is now confirmed to be a natural note; the earlier phrase "major note" is superseded. The exact reward pitch has not been assigned.

### Feasibility assessment

Suitable for a lightweight 2D browser implementation. It needs twelve clickable piano keys, a password sequence checker, two timed phases, six note wisps, four column interaction zones, and an absorption-zone overlap check. Door damage, wisps, tunnel suction, empty attempts, anger, and sleep can use simple drawings and short animations. Real fluid simulation and chasing AI are unnecessary. This is an architectural assessment, not measured performance.

Design implication: the basement now combines search order, listening, movement, absorption positioning, and time management. Empty-use consequences discourage blindly spamming the absorption button. Positive lock feedback still permits learning key positions through trial and error within the deadline; tune the time budget with that intended feedback intact.

This encounter uses mouse interaction and in-game sound playback. It does not require the microphone used for Blow the Candle.

### Phase A: door rules and PROPOSED implementation

1. Demonstration: play the melody and show each note name as specified. Do not add labels or automatic demonstration-to-key highlighting to the lock; those earlier suggestions have been superseded.
2. Safe interaction: approaching the door and opening the lock interface do not start the countdown.
3. First press: start the door countdown exactly once on the first deliberate keypress, before judging that note. All twelve keys remain playable, including incorrect ones.
4. Sequence match: maintain a progress index. A correct next note advances it and shows success feedback. A wrong note sets the index back to zero and clears all progress feedback, while the existing countdown continues. Do not silently reinterpret that wrong key as the first note of a new sequence.
5. Repeated pitches: the final `A#, A#` requires two separate presses of A#. A held button does not fill multiple sequence positions. Proposed feedback is a brief key flash plus unlabeled progress dots so repeated presses remain readable without revealing note-name labels.
6. Success: the full correct sequence before expiry stops the door timer and commits basement entry. Protect the forced jump/locking animation from a late door-timeout event.
7. Expiry: the player is caught and retries. The exact restart presentation and whether the demonstration is repeated or replayable remain OPEN.

Judging note order without exact rhythm remains a PROPOSAL. Melody length, countdown duration, and note-register policy are OPEN. An unlabeled piano intentionally challenges note-to-key mapping; do not quietly replace it with a labeled Simon-style interface. An optional earlier practice/tutorial can teach that mapping without labeling this boss's lock, but has not been approved.

### Phase B: shelf rules and PROPOSED implementation

1. Build a four-column, three-row shelf with twelve fixed slots.
2. Randomly choose six distinct slots and place five sharp-note decoys plus one natural target, with no overlapping objects. Six slots remain empty. Random placement is confirmed; when a new layout is generated on retries remains OPEN.
3. Use right-click movement to reach a column, then left-click notes in that column. Enforce the column's interaction range so the player cannot audition every shelf note from the entrance. Exact movement distance, in-range feedback, and any required column order remain OPEN.
4. Play a selected note and show its name. Auditioning any note, including a sharp decoy, does not itself collect it and does not count as a failed absorption.
5. Position the character and, if aiming is used, the absorption area. Press ABSORB/COLLECT to take out the pocket tunnel and check that area. Natural note inside: pop, disappear, absorb, restore its lantern slot, and grant an escape use. No natural note inside: play the empty reaction and record an unsuccessful absorption.
6. Repeated unsuccessful absorptions escalate to anger and five seconds of sleep. Trigger count, time window, and input restrictions are not finalized.
7. Use the earned tunnel escape. Use the fixed encounter escape scene; final activation input, scene staging, and when the timer stops remain OPEN.

PROPOSED: begin the basement countdown once the room and controls are ready; choose a separate full basement time budget rather than silently carrying over the door's remaining time. The exact timing relationship between the two phases has not been explicitly decided.

PROPOSED: distinguish empty slots visibly, mark tested notes without revealing untested names, stop the previous preview when another note is played, and lower masking music or banging during auditions. Keep the layout stationary during the search. Budget time for visiting all four columns and testing all six objects, not for a lucky first click.

### Absorption area and comic feedback

CONFIRMED: the button takes out the pocket tunnel, shows a defined absorption area, absorbs a natural note within it, and reacts to unsuccessful use. Repetition leads to an angry five-second nap. Final label is not decided; ABSORB is the current recommendation because it describes the spatial action.

PROPOSED presentation and rules:

- Make the absorption zone clear before the success/failure check, ideally with a faint positioning preview. A circle, short cone, or selected-slot area is still a design choice.
- Keep the area local enough that pressing it from the entrance cannot collect every shelf item. If it covers an entire column, the player could simply test all four columns without identifying notes. A zone aimed at one selected slot is a possible solution, but must still require the character to reach that column.
- Ensure all three shelf rows can be reached through the chosen aiming/range rules. Do not make high-row spawns impossible to absorb.
- Let wisps bob decoratively inside their slots, but use stable logical capture positions or generous boundaries so decorative motion cannot turn a well-aimed attempt into a miss.
- Snapshot eligibility at a clear action moment and lock the result. Prevent movement or decorative drift during the animation from changing a valid attempt into an empty one.
- If both a sharp and natural note overlap the area, absorb only the valid natural target. Do not report an empty area merely because a decoy was checked first.
- Each completed empty attempt counts once; button mashing during its animation is ignored, not queued as several extra failures. Holding a button must not repeatedly trigger it.
- Ordinary note auditions, empty-slot clicks, and rejected UI clicks do not count toward the angry nap.
- Suggested gag, not a fixed threshold: first empty attempt gets a blank stare, the next a shake of the tunnel, and repeated misuse makes the character pull a tiny pillow from the pocket and sleep with cartoon Zs. Example lines: "Nothing. Very impressive." and "Wake me when you find a note."
- The user fixed the sleep duration at five seconds. Proposed: movement, auditions, and absorption pause for the character while the basement danger countdown continues. Warn with visible irritation before the nap. Timer behavior and exact disabled actions still need approval.
- Discard inputs received while asleep, reset the failure streak on waking, and require a fresh press to avoid an immediate second nap from queued clicks. These reset rules are proposals.
- After success, the same button could change to ESCAPE if a manual escape use is chosen. A second button is not required. This is a proposal, not a confirmed UI flow.

### Edge cases and PROPOSED adjustments

| Risk | Proposed handling |
| --- | --- |
| Wrong notes let the player reset the deadline indefinitely | Clear only input progress; never restart the first-note countdown on subsequent presses |
| Incorrect first press fails to start danger | Trigger the countdown before checking correctness |
| Repeated B in the example is unreadable or skipped | Require separate presses; use transient key feedback and optionally unlabeled progress dots |
| Green keys leak the previous partial solution after a mistake | Clear all progress-color state when the sequence is erased |
| New players cannot map shown names to piano positions | Keep the lock unlabeled as requested; consider optional practice earlier rather than automatically revealing its answer |
| Rhythm becomes a hidden requirement | Judge order only as an initial proposal; explicitly decide any rhythm condition |
| Random generation creates too many objects or no solution | Always enforce twelve slots, six occupied, five sharp decoys, and exactly one natural target |
| Sharp spellings accidentally sound identical to the natural target | A proposed decoy set is C#, D#, F#, G#, A#, the five distinct black-key pitches. Avoid E#/B# decoys if they would sound like the natural target. Exact decoy inventory still needs confirmation |
| Character auditions another column from far away | Validate column range on each click; show inaccessible notes as out of reach and require movement |
| Clicking while between columns unexpectedly accesses two | Define unambiguous interaction zones and in-range feedback; do not let a movement destination alone grant remote access |
| Random placement or movement creates unwinnable time budgets | Keep all slots reachable and give time for worst-case four-column traversal and six auditions, with a reaction margin |
| Background music or door banging masks comparisons | Lower or simplify the soundtrack and duck banging during a short audition; show door danger visually too |
| Rapid clicking makes an unreadable chord | Stop or fade the preceding preview; show which object produced the current sound |
| All names are visible before audition | Keep names hidden until selection, preserving the user's search mechanic |
| Clicking the natural note accidentally collects it during inspection | Audition only on note click; collection requires the ABSORB/COLLECT area check |
| Absorption area bypasses the whole search or cannot reach high rows | Keep the zone local, preview it clearly, and validate reachability for all twelve slots; exact aiming remains OPEN |
| Decorative wisp movement causes arbitrary misses | Keep capture anchors stable within slots and check eligibility at a defined moment |
| A valid absorption grants several notes or escape charges on repeated clicks | Commit capture exactly once and mark the target absorbed before its pop animation |
| Repeated empty-action clicks trigger several naps | Ignore busy-state clicks, count completed empty actions once, and discard sleeping inputs; proposed reset on wake |
| Legitimate sharp-note auditions trigger the punishment | Count only failed ABSORB/COLLECT actions, not ordinary listening |
| Sleep accidentally pauses the danger timer and becomes an exploit | Proposed: keep the basement countdown running through the five-second nap; confirm before implementation |
| Capture and expiry happen together | Define a timestamp boundary, commit valid capture once, and decide whether the timer continues until a separate escape action |
| An earlier natural note permits unlimited early escapes | Each absorbed note grants one charge then travels to the lantern; spend the charge on the fixed encounter escape scene |
| Right-click movement and the lock interface conflict | Use an explicit door interaction mode; define movement cancellation and out-of-range interactions consistently |
| Player leaves the tab or audio is unavailable | Preload sounds and pause fairly so the player can hear and act when danger runs |
| Escape returns to the village or skips later bosses | Use predefined escape and next-entry scenes in confirmed order; exact staging remains OPEN |

### PROPOSED technical structure

Use clear phases: observe named melody, approach/open lock safely, enter password with active countdown, commit basement entry, search/audition/position, attempt absorption, empty reaction or successful capture, earn and use escape, or fail and retry. Add an angry/sleeping state for repeated empty actions. There is no chase phase. Each phase owns its inputs and timer so a previous phase cannot cause a late catch.

Map the twelve piano keys to note identifiers; store the password as an ordered identifier list. Keep current sequence progress separate from the countdown start/deadline. Store shelf slot, column, row, pitch, display name, and natural-target identity for each of the six objects. Shuffle a twelve-slot list and select six without replacement. Validate current player-column range before audition or absorption.

An absorption check can use a simple point/shape overlap on the note's logical position. Track action-busy state, completed empty-attempt count or streak, sleep deadline, target-absorbed flag, and earned escape-use state. No fluid simulation or per-pixel suction physics is needed. Preserve the five-second nap using elapsed time rather than frame counts.

Schedule demonstration playback using the audio clock and synchronize displayed note names to its audible events. Use elapsed-time game timers and preload sounds. Input checking and success/failure transitions should be deterministic; a lagging visual frame must not restart a timer or allow a late timeout to overwrite a committed success.

### OPEN decisions specific to this encounter

- Assign the reward note; this is confirmed encounter 2.
- The six-note password is fixed: `C#, F#, G#, D#, A#, A#`. Choose octave/register policy, rhythm requirement, playback pacing, and replay/hint behavior.
- Set the door countdown and confirm the reading that a wrong-note input reset does not reset it.
- Set the basement countdown and confirm whether it is a separate full budget.
- Confirm the five distinct sharp-note inventory, column interaction distances, audition duration, and any mandatory column order.
- Decide whether tested labels persist and whether a separate reference tone or name is useful.
- Choose ABSORB versus COLLECT, zone shape/range/aim, preview behavior, and the exact capture-check moment. All shelf rows must remain reachable.
- Set failed-absorption trigger count/time window, irritation feedback, and streak-reset rules. Sleep is fixed at five seconds; danger-timer and disabled-input behavior during sleep remain proposed.
- Basement failure restarts the whole encounter from melody observation and the lock. Decide whether random placement changes on retry.
- Stage the fixed exit scene, decide its final activation input and when the timer stops. Each note grants one charge then goes to the lantern; it is not stored in the character.
- Choose the final-boss-provided capture device/ability and the visible trapped-air art treatment.
- Define unavailable-white-key behavior under the missing-natural-pitches rule; the confirmed all-sharp password resolves the old melody conflict.

## 8. Additional guardians, final-battle proposals, and parked alternatives

The Shell Game and The Backwards Vacuum are approved at concept level. Pepper Soup is approved in the user's revised form below; the old pepper-sneeze trick is superseded. The user now counts five selected games and requests two more guardian ideas plus one final-boss game. The Crumbling Maze, The Ink Painter, and The Storm Engine below are new PROPOSALS, not approved additions. Mirror Garden, Balance the Hoard, and the earlier musical ideas remain parked. There are still only seven note guardians and one final boss.

Each guardian yields only its single stolen natural-note wisp. Use the established ABSORB/COLLECT mechanic when the note is made available; in the cooking encounter the monster releases it voluntarily after being saved. Do not invent extra natural notes. The final battle awards no eighth natural note. Music remains available for the soundtrack and recovery scenes, without being the new challenges' input mechanic. Each recovered note grants one tunnel charge then travels directly to the lantern; entry and escape scenes are predefined.

### Selected concept N1: The Shell Game - the noisy mixing machine

CONFIRMED user revision (2026-11-10): the monster has a mixing machine. After it hides its single stolen natural note under one of three shells, the machine shuffles those shells so that the monster intends only itself to know the correct one. The player can discover it by observing the shuffling animation. This is visual tracking, not an impossible hidden or unobservable shuffle. The existing small note trap can remain a proposed way to contain the airy note beneath a shell; its exact presentation remains OPEN.

Selecting the wrong shell makes the machine sound an ambulance-like alarm. The monster comes back to investigate, and the player must hide immediately. Each return has different comic expression text and attitude. CONFIRMED clarification: on the first two returns the monster shows its attitude, looks around for the cause, and puts the same natural note back into the machine. Hiding successfully allows the player to survive these two inspections. On the third return, the monster catches the player even if already hidden. The third wrong choice therefore leads to guaranteed capture on that return; hiding does not prevent it. Capture fails the attempt and restarts the entire Shell Game, including its return counter; exact failure presentation and layout regeneration remain OPEN.

Selecting the correct shell exposes the guardian's one natural note for the established ABSORB/COLLECT action. Exact access and absorption timing remain OPEN. The earlier wrong-choice treatment of junk plus a laughing monster is superseded by alarm, return, and hiding.

PROPOSED playable sequence:

1. Show the monster hide the note and the machine perform a visible, trackable shuffle. The monster leaves before the player makes a choice; exact staging remains OPEN.
2. The player left-clicks a shell after shuffling stops. Correct choice exposes the note; wrong choice triggers the alarm and begins the monster's return.
3. Right-click to reach a clearly introduced hiding place; left-click to enter it if a separate interaction is needed. Exact hiding controls are OPEN and must preserve the established mouse scheme.
4. On returns one and two, the monster performs its distinct attitude/reaction, looks around for the cause, and puts the note back in the machine. A successfully hidden player survives and can watch it leave. On return three, the monster finds and catches the player even in hiding; do not offer another ordinary retry within that attempt.
5. After either of the first two inspections, another shell choice becomes available. The monster re-hides the same note and the established mixing-machine shuffle follows. Exact placement, departure, and shuffle timing remain OPEN; the new shuffle must be observable from hiding or after leaving it. Never duplicate the note or allow a selection during the reset.

PROPOSED three-visit dialogue and visual gags, not approved final writing:

| Return | Visual gag | Expression text |
| --- | --- | --- |
| 1 | Arrives holding an enormous soup spoon | "Who called an ambulance for a shell?" |
| 2 | Arrives wrapped in a towel, still wearing a shower cap | "Someone had better be dying. I was conditioning my horns." |
| 3 | Arrives clutching a tiny pillow, looks straight at the hiding place, and pulls the player out | "Found the problem. It has legs." |

PROPOSED fairness and technical approach:

- Make a reachable hiding place visible before the first choice. Tune the first two alarm-to-arrival intervals for movement plus any hide interaction; exact timing is untested. Dialogue must not consume the player's opportunity to hide. Proposed warning after the second inspection: the monster points toward hiding spots and says, "Next time, I check EVERY corner." This signals the confirmed third-return capture without changing it; exact warning text is not approved.
- Pair the siren with a visible alarm cue and an approaching-monster cue. Use a short authored siren at controlled volume; avoid an indefinitely looping or startlingly loud sound. Exact sound is not produced yet.
- Keep all three shell paths readable, with bounded speed and no offscreen or concealed identity swaps. Track the note by shell identity, not the original screen position. The animation must agree with the correct answer.
- Accept one shell choice per attempt. Ignore additional shell clicks during the alarm, inspection, or shuffle so they cannot queue several visits or bypass hiding.
- Present alarm, approach, inspection, departure, retry, note exposure, and absorption as separate scripted states. Three shells, preplanned paths, a hiding flag, and a return counter that guarantees capture on the third return regardless of hiding are plausible for a lightweight 2D implementation; no physics or complex search AI is required. Nothing has been built or benchmarked.
- OPEN: hiding location and detection rules on the first two returns, arrival delay, search animation and duration, caught-player presentation and layout generation on whole-encounter restart, shuffle difficulty, reset/reshuffle staging, successful-choice rounds, and reward pitch. Searching and putting the note back on the first two returns, and unavoidable capture on the third, are confirmed. Do not grant additional natural notes or assume the pocket tunnel can be used before recovery.

### Selected concept N2: Pepper Soup - the starving monster's meal

CONFIRMED user revision: the cave is genuinely frightening from the entrance all the way to the throne. At the end, the supposedly terrifying monster is lying down and starving. It has eight cooking items but does not know how to turn them into a meal. The natural note is absorbed inside its body, and it refuses to give it up even while dying.

The player left-clicks the available items to collect/select them and prepares a meal in an exact ingredient order. A wrong order still produces a finished meal; it is not rejected as uncookable. When the monster eats that wrong meal, it dies and the natural note disappears. On the correct order, the meal saves the monster. It thanks the player, willingly gives the note, and reveals that it stole the note because the final boss threatened its family's lives.

The old greedy-cook, hidden-pepper, sneeze, and belt-mounted-trap premise is superseded. Do not combine it with the new encounter as though it were still confirmed. The working name Pepper Soup remains a carryover, not a finalized title for the revised story.

- Main activity: ingredient collection, interpreting recipe clues, and exact-order cooking, with a compassionate story outcome. Actual clue design is still proposed; the user specified the ordered meal and outcomes, not a final recipe.
- Controls: left-click ingredients and preparation interactions; ordinary right-click movement through the cave. The exact collection-versus-adding-to-pot interaction and final cook/serve action remain OPEN.
- CONFIRMED failure: completed wrong meal kills the monster and loses the note when eaten. Do not silently change death to sleep, turn a wrong meal into an automatic rejection, or let the player recover the note from its corpse.
- PROPOSED fairness: place findable recipe-order clues through the scary cave, allow the player to review the selected order before committing, and provide an understandable warning that the creature cannot survive a bad meal. Do not invent a random unhinted eight-item sequence or automatically reveal correctness after every ingredient without user approval.
- CONFIRMED failure recovery: a wrong meal kills the monster and destroys its note within that attempt. Restart the entire cooking encounter from its beginning, not a preparation checkpoint, restoring the monster and note for the new attempt. Do not replay earlier completed encounters or soften the failed-attempt outcome.

### Selected concept N3: The Backwards Vacuum - three puzzles and a rude awakening

CONFIRMED user revision (2026-11-10): the capture machine has a switch that reverses its function from sucking in to releasing its contents. Three puzzles are stacked one over another, with the reverse switch at the bottom. The player must solve all three to access the switch. The exact puzzle types and layouts are OPEN; the earlier valve-and-hose puzzle proposal is not a confirmed requirement.

The monster stays asleep throughout puzzle solving. After completing the puzzles and flipping the switch, the player deliberately wakes it. A simple button labeled "Wake the monster up" triggers the character to walk to the nearest column and push it. The column drops straight onto the monster's head and wakes it. This movement and push are scripted by the button; do not require a separate aiming, strength, or column-toppling mini-game.

The awakened monster tries to suck the character into its machine and presses its activation button. The machine shakes, then ejects everything because the player reversed it. CONFIRMED follow-up: it has sucked in so many things that the ejection is extremely strong. The recoil throws the monster backward into the wall and knocks it unconscious. After that impact and knockout, the character performs the absorption animation to recover the released natural note, opens the pocket tunnel, and escapes. The knockout is the confirmed opening for recovery; it does not establish a timed recovery window or a later wake-up. Flipping the reverse switch alone does not release the note: the monster's later activation causes the payoff. The reverse switch and the monster's activation button have separate roles.

CONFIRMED encounter sequence:

1. Solve the three stacked puzzles while the monster remains asleep; the reverse switch lies beneath them.
2. Flip the exposed switch to release mode.
3. Press "Wake the monster up". The character walks to the nearest column, pushes it, and it drops straight onto the monster's head.
4. The monster wakes and presses its machine's button, intending to suck the character in.
5. The machine shakes and releases everything instead, including this guardian's one natural note. The powerful ejection, caused by its accumulated contents, recoils the monster backward into the wall and knocks it unconscious.
6. After the monster is knocked out, play the character's note-absorption animation, open the pocket tunnel, and leave. This encounter ends with its predefined tunnel escape scene; the final activation input and staging remain OPEN.

PROPOSED presentation, fairness, and technical approach:

- Solving the top puzzle could remove/open its layer to reveal the next, repeating until the bottom switch is exposed. Exact layer transitions and puzzle interactions remain OPEN. Make cleared progress and the switch's changed mode readable.
- Make the wake-up button available only after all three puzzles are solved and release mode is selected. This preserves the requested simple sequence; early-wake behavior is not confirmed.
- Use a scripted straight-down column animation and a comic impact/reaction, followed by the monster confidently pressing its button. Show the strong ejection, backward recoil, wall impact, and unconscious pose as a clear sequence before absorption. Ordinary captured objects can communicate the overloaded machine; exact inventory, flight paths, and impact gags remain OPEN. Do not invent additional natural notes among the contents.
- Apply the established ABSORB/COLLECT action to recover the released note and grant the earned escape use. The absorption animation happens after the monster is knocked unconscious. Exact note landing point, whether absorption starts automatically or needs the established button press, manual versus automatic tunnel activation for this scene, and animation timing remain OPEN. Do not add a chase, monster recovery countdown, or timed collection challenge without a further decision.
- Use three puzzle completion flags, a reverse-mode flag, and scripted wake/activation/shake/ejection/recoil/wall-impact/knockout/absorption/escape states. Ignore duplicate wake presses and commit note recovery once. No falling-column physics, fluid simulation, or complex monster AI is necessary. This is a feasibility approach, not measured performance; no prototype has been built or tested.

OPEN: the three puzzle designs, solutions, hints, reset rules and difficulty; exact layer presentation; column staging and character route; ejected objects; monster expressions/dialogue; recoil and wall-impact staging; animation timing; absorption and escape inputs; fixed scene staging; and reward pitch. Encounter 4 is confirmed. The monster remaining asleep during puzzles and the deliberate column wake-up are confirmed, so do not add noise-triggered waking or a sleep countdown as established rules.

### New guardian proposal P6: The Crumbling Maze - route planning

A stone guardian keeps its natural-note trap behind a small maze. Floor tiles crumble after the character leaves them. Three switches must be reached before the central trap opens, so the player must plan a route that does not destroy the path still needed. Right-click chooses movement destinations; left-click activates reachable switches. Reaching the released note still requires ABSORB.

- Distinct activity: planning a spatial route and managing changing walkable ground. It is not a rhythm, melody, or pitch puzzle.
- PROPOSED fairness: mark fragile and permanent safe tiles clearly, show which tiles a movement command will traverse, and use a small authored layout with known solutions. If blockage is failure, restart the entire encounter under the confirmed rule; exact failure detection is proposed. Do not have pathfinding silently consume several fragile tiles the player did not intend to cross.
- Technical direction: a small tile graph, visited/collapsed flags, fixed switch states, and short crumble animations. No platforming controls or falling-bridge physics are necessary.
- OPEN: maze layout, switch count, whether a timer is needed, failure presentation, and reset behavior. Three switches is a proposal, not a requirement.

### New guardian proposal P7: The Ink Painter - dodge and counter

A chibi cartoon monster paints dangerous shapes onto the floor with an oversized brush. The player right-clicks safe places to avoid clearly previewed strokes and ink patches. After each painting attack, the monster pauses to dip its brush; this is the window to left-click a reachable rinse valve. Water washes away part of its ink armor. After several successful counters, the armor opens around its note trap and the player can reach and absorb the wisp. The dramatic monster could end as an indignant tiny ink blob.

- Distinct activity: readable real-time evasion plus choosing a counter opportunity, rather than repeating a password or solving a static machine.
- PROPOSED fairness: telegraph attack areas before they become dangerous, let action windows account for movement time, and start with one simple brush pattern. Give safe recovery space and avoid attacks covering every accessible destination. Define damage/retry without requiring pixel-perfect timing.
- Technical direction: a few authored attack shapes, point/shape collision checks, a boss attack/recovery state, and armor stages. Use fixed ink puddles and sprite/vector poses, not real liquid simulation.
- OPEN: number of counters, movement/path preview, hit penalty, vulnerability duration, exact trap opening, and whether a cornered-player safety rule is needed.

### Final-boss proposal P8: The Storm Engine - survive, sabotage, reverse

This is a proposed finale for the confirmed eighth boss and its army after the village's apparent victory. All seven natural notes have already been recovered; there is no eighth note to collect. The boss brings a gigantic version of its capture machine, the Storm Engine, intending to suck the recovered power away again. The exact location remains open.

Proposed three-phase battle:

1. Survive the assault: army attacks and storm strikes are visibly telegraphed. Right-click moves between safe cover; left-click nearby gates or barriers to block incoming groups. Show the larger army in background silhouettes and operate only a few active threats at a time.
2. Sabotage the machine: reach several control points and change valves while avoiding the boss's attacks. The Backwards Vacuum introduces reversing a capture machine; any finale valve mechanics would be new, since the Vacuum's three puzzle types remain OPEN. The final machine should have new positioning and danger rather than replaying that entire encounter.
3. Reverse the storm: after the controls are ready, bait a large, visibly aimed boss attack into its own exposed engine fitting and step away. This exposes the reverse lever. Activate it to turn the engine against the boss, collapse the storm, and finish the encounter. The seven restored notes can sound together in the victory scene without requiring a musical-input puzzle or consuming the recovered notes.

- Story proposal: the saved starving guardian may return to help with a gate, distraction, or warning about the machine. Its participation and whether other guardians assist are not confirmed. Do not assume the whole army was coerced or automatically defects; mixed guardian loyalties are confirmed, but only the starving guardian's specific family-threat story is assigned.
- PROPOSED fairness: clear phase transitions, protected success animations, visible threat previews, reachable controls, and warnings. Failure restarts the whole final encounter including all phases, without phase checkpoints; earlier completed guardians are not replayed. Keep the encounter straightforward.
- Technical direction: a few active attack patterns, preplanned army-wave events, valve states, cover states, and staged engine/boss animations. No mass-army simulation or new note generation is required.
- Constraints: do not absorb the boss as if it were a natural note, require a new natural-note pickup to recharge an escape, consume the seven notes, or introduce a tunnel combat power without a new explicit design decision. Defeating the engine ends the fight in this proposal.
- OPEN: final-boss identity/motive, location, attack patterns, number of mechanisms, army presentation, ally participation, retries, exact final reversal, and post-battle ending. All three phases are unapproved proposals.

### Parked option N4: The Mirror Garden - redirect sunlight

A gardener monster keeps the note trap enclosed in a stubborn, thorny plant. The player rotates garden mirrors to bring sunlight to several marked buds. When the required buds receive light, the plant unfolds and reveals the trap. The monster can respond by indignantly putting sunglasses on the flower.

- Main activity: spatial light-routing and environmental logic.
- Controls: right-click between mirror stations; left-click to rotate each mirror through a few fixed positions.
- Fairness proposals: preview beam paths, make reachable mirror positions clear, and use a small authored layout with a guaranteed solution. Give gradual flower feedback rather than a completely silent all-or-nothing outcome. Distinguish this puzzle from the candle's shadow-detection mechanic.
- Technical direction: a small fixed-angle ray or connection puzzle, line drawings, and a plant-opening animation. Realistic reflections and plant simulation are unnecessary.
- OPEN: mirror count, whether buds need light simultaneously, monster interference, and any timer.

### Parked option N5: Balance the Hoard - lower a hanging platform

A hoarding monster keeps the note trap on a hanging platform above the character's reach. By moving sacks or treasures onto the counterweight, the player brings the platform level with a walkway. The player then approaches it, opens or accesses the trap, and absorbs the note. The monster's comic interference could be to add one tiny coin and act as if it has ruined everything.

- Main activity: weight balancing, object placement, and planning a route to the prize.
- Controls: left-click to pick up/place a sack at a marked location; right-click to carry it between stations. Dragging or platformer controls are not required.
- Fairness proposals: readable weight or balance indicators, reversible item placement, no crate-pushing softlocks, and a stable access interval. Keep all necessary objects reachable; if a monster adds weight, telegraph the change and make recovery possible.
- Technical direction: authored weight values, fixed placement slots, and a platform animation driven by the balance state. Full rigid-body or rope physics is not needed.
- OPEN: weight rules, carrying behavior, the trap-opening step, monster interference, and any time pressure.

### Selection status and lore boundary

Five games are selected, including the revised cooking story, The Backwards Vacuum, and The Shell Game. The Crumbling Maze and The Ink Painter are the current suggestions for the two remaining guardians; The Storm Engine is the current final-battle suggestion. They still need user selection. Mirror Garden, Balance the Hoard, and the musical concepts below remain parked rather than being quietly added to the roster.

One natural-note energy per guardian and the loss of stolen natural pitches from instruments are confirmed. Do not generate extra notes or assume instruments can imitate missing natural pitches. Review parked musical ideas against this rule before any future selection.

### Earlier musical options - parked, not selected

The user liked the earlier suggestions but requested a non-musical direction after clarifying ownership of the natural notes. The five concepts below are preserved for reference and possible later adaptation. They are not the active recommendation and must not be implemented without selection and a lore-consistency review.

### Candidate A: The Jealous Drummer - rhythm duel

A proud monster powers its note trap with an enormous drum and challenges the character to a performance. It plays a short rhythm; the player answers on a little drum with left-clicks. Pauses are part of the phrase: clicking during a rest is a mistake. Several successful exchanges disrupt the trap and release the natural note. After defeat, the monster could sulk because the tiny drum got the better applause.

- Distinct activity: reproduce timing and rests, not pitch names or a piano password.
- Controls: left-click the drum; ordinary right-click movement brings the character to the playing spot.
- Fairness proposals: visible beat cues, a practice phrase, generous timing tolerance, no damage from a single miss, and no rapid-click shortcut. Difficulty can add a rest or a longer phrase rather than require extreme precision.
- Technical direction: a small authored rhythm list, scheduled sound playback, timestamped click comparison, and simple drum animations. Account for audio/output latency before setting tight windows. Do not judge hit timing by the visual frame when the animation renders.
- OPEN: phrase length/count, error recovery, visual assistance, and the exact threshold for releasing the trap.

### Candidate B: The Broken Music Box - arrange a song

A hoarding monster keeps the note inside a music box, but its melody strip has broken into pieces. The player clicks four short song fragments to audition them and swaps two selected pieces with left-clicks to rebuild the tune. An anchored opening and ending, with fragments sharing small musical phrases at their joins, provide clues. Completing the arrangement makes the box play its full song and open the note trap.

- Distinct activity: reconstruct musical structure and continuity, rather than memorize a demonstrated keyboard sequence.
- Controls: left-click to preview and select/swap fragments; dragging is not necessary.
- Fairness proposals: use authored fragments with one intended solution and clear joins. Fix the first and last pieces initially. Distinguish Listen and Swap modes so inspecting a piece does not unexpectedly move it. A winding key slowly running down could provide pressure after a safe introduction; a timer is not yet chosen.
- Technical direction: a few preloaded audio fragments, ordered slots, a permutation check, and a playback preview. Align cuts and sound envelopes so the correct arrangement does not contain accidental gaps or clicks.
- OPEN: fragment count, whether to use a reference song, preview controls, and winding/failure rules.

### Candidate C: The Echo Pipes - route a melody

A monster's trap feeds stolen music through a tangled pipe machine. The player sends a short tune into the inlet and rotates pipe junctions with left-clicks to route it toward the note's chamber. Wrong routes send the tune to silly outlets, such as a snoring horn or a kettle whistle. A complete route delivers the melody to the chamber and opens it.

- Distinct activity: spatial planning and following sound through a machine.
- Controls: left-click reachable junctions to rotate them; right-click movement between control stations if the scene uses more than one.
- Fairness proposals: show a small pulse moving with the audible tune so the route can be followed without relying on stereo headphones. Wrong outputs give useful feedback. Use a bounded authored graph rather than unconstrained pipe generation; ensure the puzzle has a reachable solution. Keep continuous fault sounds short.
- Technical direction: simple graph connectivity and staged pulse animations with short sound effects. No real acoustic reflection simulation or fluid simulation is needed.
- OPEN: pipe count, reach limits, whether junctions can change while the tune is traveling, and any timer. Candidate risk: music must provide route feedback so the scene retains a musical identity instead of becoming a generic pipe puzzle.

### Candidate D: The Off-Key Organ - tune the monster's machine

A monster uses a wheezing organ to keep the stolen note trapped. Three pipes are out of tune. The player hears a reference tone for one pipe, then adjusts that pipe higher or lower using clickable controls. When the three pipes are tuned, the organ plays a stable chord that cracks open the note trap. The monster might blame the instrument while the repaired organ keeps interrupting its complaints.

- Distinct activity: compare and adjust pitch, not identify a note without a reference.
- Controls: left-click reference playback and higher/lower controls; right-click movement between stations if desired. Singing or an additional microphone mode is not required.
- Fairness proposals: offer reference playback and clear feedback that improves near the target. Use a tolerance band, not a single exact value. Keep the timbre and volume comparable. Allow step buttons so a slider is not the only interaction.
- Technical direction: simple tone/sample playback, a tunable pitch value, and target-range checks. No pitch recognition of the player's voice is needed. Generate playable detuning and useful feedback rather than rely on absolute pitch or expert hearing.
- OPEN: whether pipes are adjusted independently or influence one another, pressure/timer rules, pitch range, and feedback assistance.

### Candidate E: The Noisy Orchestra - separate musical layers

A conductor monster surrounds the stolen note with a chaotic little orchestra. The player hears a short reference melody leaking from the trap. Five performers play separate looping parts; two together contain that melody, while the others mask it. Left-clicking the performers mutes or solos their parts. Finding and leaving the correct pair playing lets the melody emerge clearly and unlocks the trap. Silenced performers can react with offended cartoon expressions.

- Distinct activity: isolate instruments and recognize how two musical layers fit together.
- Controls: left-click performer controls; no need for vocal input or fast clicking.
- Fairness proposals: introduce performers separately before combining them. Keep their mute/solo state visible and provide short reference playback. Give feedback when the target melody is clearer. Ensure the intended combination is audibly understandable and unique; an optional later round could change the instrumentation.
- Technical direction: author synchronized instrument stems and control their gains. These must be separate tracks or synthesized parts from the start, not an attempt to extract instruments from one finished recording. This concept needs more soundtrack preparation than the other candidates.
- OPEN: performer count, correct combination size, hint/feedback rules, and any time pressure. Five performers and a target pair are initial proposals only.

### Earlier musical shortlist and general rules - parked

The earlier shortlist was The Jealous Drummer, The Broken Music Box, and The Off-Key Organ. It is parked with the other musical proposals. None of those musical concepts is selected. See the current selected roster and remaining three proposals above.

All five are intended as small 2D scenes with a few sound sources, bounded objects, and simple animations. This makes them plausible candidates for the low-spec direction, but none has been implemented or benchmarked. Keep musical clues replayable where appropriate, avoid exact-pitch guessing without a reference, and preserve the established right-click movement/left-click interaction scheme. Exact difficulty and timing need playtesting.

## 9. Microphone technical plan

The user has chosen microphone strength input and authored sound output. The following implementation details are PROPOSED and need prototyping:

- Request microphone access before the encounter. A hosted browser game normally needs HTTPS, plus user permission.
- Calibrate room noise and one short, comfortable practice breath. Display a microphone meter and detection feedback.
- Analyze level, duration, and frequency distribution locally using Web Audio. No speech recognition, recording, or upload is required for this design.
- Estimate a likely breath rather than triggering on every loud sound. Speech, claps, fans, and music can still produce false positives; do not promise perfect blowing recognition.
- Normalize strength for the individual microphone. A short measurement window can determine strength before the authored effect plays.
- One accepted breath produces one gust. Ignore retriggers during the authored puff sound, require a recovery interval, and rearm only after quiet input.
- Strength could control gust size, authored effect volume, or soft/medium/strong sound variants. Extinguishing threshold and strength-dependent range are OPEN. Do not require maximum-force blowing.
- Allow for detection latency in the boss's reaction window.
- Test built-in and headset microphones and speaker playback. Headphones may help with sound leakage.
- Test noise suppression and automatic gain settings because voice processing may weaken blowing noise. Echo cancellation may help but is not guaranteed to remove game audio.
- Stop microphone capture when leaving the encounter; handle missing devices, denied permission, disconnection, and backgrounding without unfair failure.
- A fallback control is recommended but not finalized.

## 10. Visual, audio, and performance approach

The whole game can be implemented with web technology; external art or music tools are optional. Specific libraries and frameworks are not chosen.

### CONFIRMED visual direction

On 2026-11-10 the user chose 2D cartoon art, chibi style, and pastel colors, replacing the earlier doodle direction. This applies to the game's overall visual presentation. Soft music and the low-spec browser target remain confirmed.

### PROPOSED visual treatment and OPEN details

- Chibi characters and monsters could use large heads, small bodies, rounded forms, and expressive faces. Exact proportions and individual designs remain OPEN.
- A possible palette uses soft peach, mint, lavender, pale blue, and warm cream. These colors are examples, not an approved palette; exact colors and outline treatment remain OPEN.
- Keep interactive objects, hazards, shadows, and feedback legible against pastel scenery. The revised cooking cave must still feel frightening from entrance to throne; the style change does not revise its story or outcomes.
- Use restrained shading, small pose sets, and limited effects as a proposed lightweight approach. No art pipeline has been selected, no new visual assets have been produced, and performance remains unmeasured.

| Area | PROPOSED approach |
| --- | --- |
| Characters and monsters | SVG, Canvas drawings, or sprites with chibi proportions, expressive faces, rounded silhouettes, and clean outlines |
| Environments | Layered 2D cartoon scenery in pastel colors, with simple shapes and restrained shading |
| Animation | Small pose sets; blinking, bouncing footsteps, swaying plants, flickering flame |
| Rain and magic | Limited droplets, line strokes, musical symbols, inexpensive glows |
| Menus and dialogue | HTML and CSS |
| Audio | Web Audio notes and layers; recorded samples or composed tracks for richer sounds |
| Low-spec performance | Cache backgrounds and silhouettes; cap rendering resolution and particles; avoid costly blur effects; test on older hardware |

PROPOSED first prototype: one polished cave encounter with movement, candle and shadow interaction, microphone strength input, authored sound, note absorption, and one lantern slot restoring remotely. This prototype has not been built or scheduled.

### CONFIRMED cutscene production preference

Keep animation code as small and simple as practical for the web and low-spec devices. The Vacuum wake-up button starts one noninteractive sequence: character moves to column, hits/pushes it, column drops onto monster's head, monster wakes angry, grabs machine, presses button, machine shakes and blasts contents everywhere, recoil throws monster into wall, monster becomes unconscious. Absorption and the fixed escape follow. A short video/clip or simple authored animation is acceptable; the user prefers simple optimized animation when practical. No format or runtime library is chosen.

PROPOSED production check: compare a short compressed clip against a small sprite/pose sequence for download size, memory, playback smoothness, and transition into absorption on target hardware. Avoid complex procedural animation or physics. No clip, animation assets, implementation, or performance measurements exist yet.

### Web design and animation skills: researched options

The user asked about skills for web design and animation, including Motion. The following is tooling research dated 2026-10-22, not a finalized dependency choice or authorization to install tools.

An agent skill supplies reusable guidance and workflows for the AI. An animation library supplies code that runs in the game. Installing a guidance skill does not by itself add runtime animation code or guarantee low-spec performance.

| Option | Availability observed in this chat | Possible APFS use |
| --- | --- | --- |
| Product Design skills | Already available in the current session | Explore visual directions, turn a selected mockup into frontend code, and review screens |
| ImageGen skill | Already available in the current session | Produce optional raster reference art, character concepts, or background assets |
| Sites skill | Already available in the current session | Build browser experiences and optionally publish when requested; no site has been built for APFS |
| Official Motion skill / Motion AI Kit | Verified in Motion's official documentation; not loaded or installed by this task | Animation guidance and current documentation access; optional advanced editing and performance tooling |
| Motion JavaScript library | Researched, not installed or selected | Coordinate HTML/SVG transitions and optional animated object properties; a React dependency is not required for its JavaScript API |

Motion's official documentation states that the skill and installer are free/open source and basic documentation search is free. Advanced CSS spring tooling, performance audits, transition editing, and premium example source are Motion+ features. Do not imply those paid capabilities are already available. A broad plugin-directory search also returned design/media integrations, but no additional plugin connection was needed or configured.

PROPOSED combination: Product Design for visual exploration, Canvas 2D for the gameplay scene and timing, CSS for small ambient loops, and Motion selectively for coordinated SVG/interface animation. This is a recommendation, not an adopted stack. The low-spec goal still requires measuring the resulting game on older hardware. No skills, animation packages, or MCP servers were installed during this research.

## 11. Progress and next work

### Completed design work

- Chosen the working game title and broad art/audio direction. On 2026-11-10, the user replaced doodle art with 2D cartoon art, chibi characters, and pastel colors. No visual assets or game implementation have been created for this change.
- Recorded the user's seven-note story and eight-round structure.
- Replaced repeated home visits with note absorption and remote lantern recovery.
- Reviewed Blow the Candle for technical feasibility and edge cases.
- Recorded and reviewed Press to Find Matching Sounds, then incorporated the user's corrections: no chase, unlabeled twelve-key lock, named demonstration, input reset feedback, a six-object randomized shelf, and pocket-tunnel escape.
- Added airy trapped-note forms, final-boss-provided sucking devices/abilities, an area-based ABSORB/COLLECT action, an earned escape use, and comic empty-attempt reactions ending in a five-second nap. This replaces automatic pickup on note click.
- Recorded mouse movement/interaction and microphone strength with authored sound.
- Created human HTML documentation and this portable AI handoff.
- Designated `C:\Users\JoseKim\Desktop\APFS` as the project folder.
- Researched available web-design skills and Motion's official AI Kit; recorded optional uses and free/paid boundaries without installing or selecting new tooling.
- At the user's request, proposed five musical encounter candidates: rhythm duel, song-fragment arrangement, melody-routing pipes, organ tuning, and instrument-layer isolation. None has been chosen.
- Incorporated the confirmed one-natural-note-per-guardian constraint and the user's request for non-musical challenges. Parked the earlier musical options and proposed five physical/comic alternatives: The Shell Game, Pepper Soup, The Backwards Vacuum, The Mirror Garden, and Balance the Hoard. Flagged the existing basement password for lore review; no established encounter was silently replaced.
- The user approved The Shell Game and The Backwards Vacuum and replaced Pepper Soup with exact-order cooking for a starving monster, including wrong-meal death/note loss and a family-coercion reveal on success. The selected roster now contains five games. Proposed The Crumbling Maze and The Ink Painter for the last two guardians, and The Storm Engine for the finale; those three are not chosen yet.

- Refined The Shell Game with the user's three-shell mixing machine, ambulance-like wrong-choice alarm, immediate hiding, and up to three different monster return reactions. Confirmed that the first two returns include attitude, searching, and putting the note back; the third return catches the player even when hidden. Warnings are required; exact dialogue, warning presentation and reset staging remain proposed. Capture restarts the whole encounter; exact failure presentation remains open.

- Revised The Backwards Vacuum with three stacked puzzles over a reverse switch, an always-sleeping puzzle-phase monster, a simple wake-up button and scripted falling-column gag, monster-triggered overloaded ejection and recoil into a wall, unconscious monster, and an absorption animation followed by tunnel escape. Puzzle designs and detailed timing/inputs remain open; no implementation or testing has occurred.

- Confirmed missing-natural-pitch lore, Monster King and mixed guardian loyalties, direct note transfer and one-use fixed escapes, predefined entry scenes, whole-encounter restarts, warnings and order 1-5. Added section 16 for scenes/backstories and the simple web cutscene production direction. No implementation or testing has occurred.

### Current next step

Develop section 16: each monster's entry/escape scene, personal story, and loyalty or coercion, following confirmed order 1-5. Select the remaining guardians and final-battle mechanics separately. Use the confirmed all-sharp basement password, define unavailable-white-key behavior, and design the three Vacuum puzzles. Keep encounters straightforward with full current-encounter failure restarts and warnings. Do not start full implementation from planning alone.

### Remaining design and validation

- Scene staging and individual backstories in section 16; protagonist identity and king's theft motive.
- Select guardians 6 and 7 and final battle. The Crumbling Maze, The Ink Painter, and The Storm Engine remain unselected.
- Define unavailable white-key behavior and when recovered natural pitches return to instruments. The six-note all-sharp basement password is confirmed.
- Design three stacked Vacuum puzzles and simple wake-to-knockout cutscene; choose clip versus authored animation after evaluating web performance.
- Cooking ingredients, exact recipe, clues, pre-serving warning, and success/failure staging. Failure restarts the entire encounter.
- Shell hiding/search rules and timing, distinct reaction text, warning before the third-return capture, and whole-encounter restart presentation.
- Lock and basement timers, octave policy, exact sharp-note inventory, absorption zone/button and failed-use thresholds; five-second sleep inputs and danger-timer behavior.
- Fixed entry/escape staging, final escape activation input, and timer-to-success boundary.
- Microphone reliability, fallback controls, candle timing and detection, movement cancellation, and range.
- Reward pitches, note naming, monster identities, final location, army motives and ending.
- Visual assets/prototype and performance measurements on representative older hardware. Nothing is implemented or benchmarked.

## 12. Documentation maintenance and handoff

CONFIRMED user preference: keep both the readable HTML and AI Markdown updated so progress can continue in other places.

For every material design decision or implementation milestone:

1. Update this Markdown record with the current state, distinguishing CONFIRMED, PROPOSED, OPEN, and SUPERSEDED items.
2. Run `python build_docs.py` in the project folder to regenerate the human HTML from this Markdown, with the same version and update date. The helper retains the existing HTML styling and embeds the source hash to check synchronization. If Python is unavailable, update the HTML directly to match.
3. Record real implementation and validation results. Do not present unbuilt or untested behavior as complete.
4. Keep the canonical files together in the project folder. Copies shared elsewhere are snapshots, not additional independent masters.
5. Preserve user edits and reconcile differences before overwriting.
6. Keep enough context for a new AI to continue without the original conversation.

Portability: give another AI `GAME_DESIGN.md`, or the whole APFS folder. It should read this file and `AGENTS.md`, then continue from section 11. The Windows project path identifies the current location; if the folder moves, update that path and preserve the relative companion filenames. These files carry context; they do not create automatic background syncing across computers or chats.

## 13. Superseded directions

- Basement password example `C, D#, G, A#, B, B` and unselected status of the all-sharp alternative: replaced by the confirmed six-note password `C#, F#, G#, D#, A#, A#`.
- Instruments freely imitating stolen natural pitches, notes staying inside the protagonist, stored-note tunnel recharge, free destination selection, undecided order 1-5 and intermediate-stage failure checkpoints: replaced by the confirmed rules in version 0.17.
- Backwards Vacuum valve/hose configuration and player-triggered immediate release: replaced by three stacked puzzles hiding a reverse switch, a deliberately awakened monster, and the monster activating the reversed machine before note recovery and tunnel escape.
- Shell Game ambiguity about the three-return cap: resolved by the user. The first two inspections allow hiding and reset the note; the third guarantees capture even when hidden. The earlier proposed third-visit line threatening one more alarm is replaced with a capture gag.
- Shell Game wrong choices merely revealing junk and making the monster laugh: replaced by the mixing machine's ambulance-like alarm, the monster returning to investigate, and immediate hiding.
- Doodle art style: replaced on 2026-11-10 by 2D cartoon art with chibi characters and pastel colors. Earlier doodle-specific presentation suggestions should follow the new direction.
- Collecting ordinary village noises as the main objective: replaced by seven stolen base notes and monster encounters.
- A lonely creature collecting sounds for a lullaby as the main ending: replaced by the eighth boss and army.
- Repeated playable returns home between bosses: rejected in favor of an outward journey and remote recovery.
- Keyboard-first blowing: replaced by microphone strength input. A button remains only a proposed fallback.
- Playing raw microphone audio as the character sound: not the intended design; use our authored effect.
- A playable chase during the melody lock: explicitly rejected; use a countdown that begins on the first player note.
- Labeling the lock or automatically highlighting matching keyboard positions during the monster's demonstration: replaced by displayed note names/sounds during the demonstration and an unlabeled piano lock.
- Earlier automatic win/absorption/escape on the correct note audition: replaced by the user's ABSORB/COLLECT area check, successful absorption, and earned tunnel escape use. Automatic versus manual use of that escape remains OPEN.
- Unspecified basement object count: replaced by twelve shelf slots containing six objects (five sharp decoys, one natural target).
- Treating the natural target as an unconfirmed interpretation of "major note": resolved by the user's explicit natural-note clarification.
- Original Pepper Soup trick (greedy cook, hidden pepper, sneeze, belt-mounted trap): replaced by the user's starving monster with a note contained in its body, an exact-order meal, lethal failure, and voluntary note gift plus family-threat revelation on success.
- Earlier statement that no additional guardian concepts were selected: the user has now approved the revised cooking encounter, The Backwards Vacuum, and The Shell Game, bringing the selected count to five.

## 14. Revision history

| Version | Change |
| --- | --- |
| 0.1 | Recorded story, lantern, visuals, and candle encounter review |
| 0.2 | Added right-click movement, left-click interaction, and microphone blowing direction |
| 0.3 | Clarified microphone strength input versus authored blowing sound output |
| 0.4 | Added portable Markdown, synchronized documentation workflow, persistent project instructions, and APFS project folder |
| 0.5 | Recorded and reviewed the melody-password and timed basement encounter; updated encounter counts and unresolved musical rules |
| 0.6 | Applied the user's lock/countdown corrections, named melody with unlabeled piano keys, 4x3 shelf containing six randomized notes, automatic victory, and natural-note-powered pocket tunnel |
| 0.7 | Added trapped-air note forms, final-boss capture devices/abilities, a spatial ABSORB/COLLECT action, earned tunnel escape, and comic failed attempts with a five-second nap; superseded automatic pickup on audition |
| 0.8 | Recorded available design skills and official Motion animation-skill research; no installation or final stack choice |
| 0.9 | 2026-10-23: proposed five distinct musical mini-games at the user's request; all remain unselected options |
| 0.10 | Confirmed one natural note per guardian, shifted current ideation to five non-musical physical/comic puzzles, parked earlier music candidates, and flagged the basement password for lore consistency |
| 0.11 | Recorded three more selected concepts, the user's starving-monster cooking rewrite and family-threat motive; proposed two remaining guardian games and a three-phase final Storm Engine battle |
| 0.12 | 2026-11-10: replaced doodle art with the user's confirmed pastel 2D cartoon/chibi direction; updated visual suggestions and retained open art details and untested performance status |
| 0.13 | 2026-11-10: refined The Shell Game with a three-shell mixing machine, ambulance-like wrong-choice alarm, hiding, and up to three distinct comic monster returns; recorded proposed dialogue and open retry/cap rules |
| 0.14 | 2026-11-10: confirmed two Shell Game inspections with attitude, searching, and note reset; third return guarantees capture even in hiding; revised proposed final gag and left post-capture retry rules open |
| 0.15 | 2026-11-10: revised The Backwards Vacuum with three stacked puzzles, a bottom reverse switch, sleeping monster, wake-up button and falling-column gag, monster-triggered ejection, note recovery and tunnel escape; puzzle specifics remain open |
| 0.16 | 2026-11-10: confirmed that the Backwards Vacuum's overloaded ejection recoils the monster into a wall and knocks it unconscious before the character's absorption animation and tunnel escape |
| 0.17 | 2026-11-10: confirmed missing natural pitches, Monster King and mixed loyalties, direct note transfer and one-charge fixed transitions, whole-encounter restarts, warnings and order 1-5; added scene/backstory section and simple web cutscene production preference |
| 0.18 | 2026-11-10: recorded an all-sharp melody as a proposed lore-compatible piano password; exact sequence and unavailable-white-key behavior remain unselected/open |
| 0.19 | 2026-11-10: confirmed encounter 2 password C#, F#, G#, D#, A#, A#; updated repeated-key guidance and resolved the old melody lore conflict; unavailable-white-key behavior and timing remain open |

## 15. Technical references

- [Canvas optimization](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas)
- [Canvas transformations](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/transform)
- [SVG guides](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides)
- [Web Audio best practices](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices)
- [Microphone capture and permission](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [Frequency analysis](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/getFloatFrequencyData)
- [Right-click context menu behavior](https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event)
- [Accidentals and natural notes](https://musictheory.pugetsound.edu/mt21c/Accidentals.html)
- [Enharmonic pitch equivalents](https://musictheory.pugetsound.edu/mt21c/EnharmonicNotes.html)
- [Web Audio sequencing and scheduling](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques)
- [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Official Motion AI Kit](https://motion.dev/docs/ai-kit)
- [Motion AI Kit installation and free/paid features](https://motion.dev/docs/ai-kit-install)
- [Motion JavaScript animation API](https://motion.dev/docs/animate)

## 16. Encounter scenes and monster stories

This is the dedicated scene/backstory workspace requested by the user. Confirmed scenes are below; unresolved individual stories remain OPEN. Each monster encounter has a predefined entry scene and, after successful note recovery, a predefined tunnel escape. These are authored transitions, not extra navigation puzzles. Exact staging is OPEN; entry is not automatically a tunnel action.

### Shared story and continuity rules

- CONFIRMED: the Monster King is the world's most powerful monster. His seven guardians serve under threat of death for disobedience. Some also respect him; some are good monsters forced to steal. Do not give them all the same motive or assign individual loyalties without a decision.
- CONFIRMED: stolen natural notes stop the lantern illuminating the world and leave instruments with sharp notes. Absorption gives one tunnel charge then sends the airy note directly to the lantern; the character does not retain it.
- CONFIRMED: failure restarts the current encounter from its beginning, including all stages, without stage checkpoints. Earlier completed encounters are not replayed. Keep the games straightforward enough to support this rule.
- CONFIRMED: warn players before dangerous or irreversible outcomes, including the Shell Game's third-return capture. Exact text, indicators and timing remain OPEN.
- OPEN: protagonist name/background; king's theft motive; guardian names, personal loyalties and fates; restoration timing of instrument pitches; final location and ending.

### Encounter 1: Blow the Candle

CONFIRMED scene: cave, huge candle, guardian facing a wall, protagonist's shadow revealing their presence. Extinguish the repeatedly relit candle and recover note C. Fixed entry and tunnel escape frame the encounter; exact staging remains OPEN.

OPEN monster story: name, why it watches the wall, respect versus forced service to the king, and reaction to losing the note.

### Encounter 2: Press to Find Matching Sounds

CONFIRMED scene: observe the guardian's named melody at the lock; solve the unlabeled piano lock; jump into the basement and become locked in; search the shelf while the guardian tries to break through; absorb the target and use the fixed escape. Failure in either stage restarts the whole encounter from its beginning.

OPEN monster story: name, why it stores notes in a basement, individual loyalty/coercion, and what the player learns about it. The confirmed password is `C#, F#, G#, D#, A#, A#`; the earlier multi-natural-note example is superseded. Unavailable white-key behavior remains OPEN.

### Encounter 3: The Starving Monster's Meal

CONFIRMED scene: frightening cave from entrance to throne; starving guardian lying at the end; eight ingredients and exact-order cooking. Correct meal saves it and earns a voluntary note gift. Wrong meal kills it and destroys its note within that failed attempt, then the entire encounter restarts. Successful recovery leads to the predefined escape.

CONFIRMED personal story: the king threatened its family to force it into theft. OPEN: name, family details, why it is starving, recipe clues, and any future finale involvement.

### Encounter 4: The Backwards Vacuum

CONFIRMED scene: sleeping guardian, three stacked puzzles and bottom reverse switch. Once reversed, the wake-up button starts the authored column-to-knockout sequence in section 10. Absorb the released note after the monster becomes unconscious, send the note to the lantern and spend the charge on the fixed escape. Exact puzzles, cutscene medium and absorption trigger remain OPEN.

OPEN monster story: name, why it collects so much, why it sleeps here, and whether it respects the king or serves unwillingly. Its comic defeat does not establish its moral alignment.

### Encounter 5: The Shell Game

CONFIRMED scene: note hidden beneath a shell, machine shuffles three shells, wrong choice sounds an ambulance-like siren. First two returns include distinct attitudes, looking for the cause and putting the note back; hiding protects the player. Third return catches the player even in hiding and restarts the whole encounter. Give a warning before this consequence. Correct choice leads to absorption and the fixed escape.

OPEN monster story: name, purpose of the machine, personal loyalty/coercion, final dialogue and capture gag. Suggested spoon, shower-cap and pillow entrances remain proposals.

### Guardians 6 and 7, and the Monster King

OPEN/unselected: The Crumbling Maze and The Ink Painter remain candidate scenes. The eighth encounter features the king and his army after the restored village celebrates; The Storm Engine mechanics remain a proposal. There is no eighth natural note. Decide final entry, battle, army motives, guardian assistance and ending separately. A multi-stage final encounter also restarts from its beginning on failure.
