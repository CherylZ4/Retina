import cohere
import keys
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
Word: Eye
Definition:""",
  temperature=0.8,
  max_tokens=100,
  stop_sequences=["--"]
  )
print(response.generations[0].text)
