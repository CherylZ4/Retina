import cohere
import keys
def grabDefinition(word: str):
  co = cohere.Client(keys.cohereapikey)
  response = co.generate(
    model='xlarge',
    prompt=f"""
This program generates the definition of the given word
--
Word: Laptop
Definition: A portable computer, usually battery-powered, small enough to rest on the user's lap and having a screen that closes over the keyboard like a lid
--
Word: Cup
Definition: A small, open container made of china, glass, metal, etc., usually having a handle and used chiefly as a receptable from which to drink tea, soup, etc.
--
Word: Chair
Definition: A seat, especially for one person, usually having four legs for support and a rest for the back and often having rests for the arms.
--
Word: Bottle
Definition: A portable container for holding liquids, characteristically having a neck and mouth and made of glass or plastic.
--
Word: Bench
Definition: A long seat for several people.
--
Word: Comb
Definition: An implement used for the dressing of hair, having a toothed or otherwise formed edge or surface, set in a handle of some material.
--
Word: Tie
Definition: A long narrow piece of cloth or other material worn around the neck.
--
Word: Elevator
Definition: A platform or cage, usually operated by electricity, in a shaft and used for raising and lowering people or things to different levels.
--
Word: Post
Definition: A piece of wood, metal, concrete, etc., driven into the ground
--
Word: Sign
Definition: A communication by words or symbols, written, painted, or drawn, or expressed in any other form.
--
Word: Car
Definition: An automobile, especially a closed, four-wheeled passenger car powered by an internal-combustion engine and designed to carry a small number of people.
--
Word: Clothing
Definition: Items worn to cover the body, usually for warmth or decency.
--
Word: House
Definition: A building or structure in which people live.
--
Word: Garden
Definition: A plot of ground where herbs, fruits grow.
--
Word: {word}
Definition:""",
    temperature=0.8,
    max_tokens=50,
    stop_sequences=["--"]
    )
  return (response.generations[0].text.strip('--').strip('\n').lower())