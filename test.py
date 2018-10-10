from summarizer import summarize

text="""
  When Microsoft Senior Vice President Steve Ballmer first heard his company was planning to make a huge investment in an Internet service offering movie reviews and local entertainment information in major cities across the nation, he went to Chairman Bill Gates with his concerns.

After all, Ballmer has billions of dollars of his own money in Microsoft stock, and entertainment isn't exactly the company's strong point.

But Gates dismissed such reservations. Microsoft's competitive advantage, he responded, was its expertise in "Bayesian networks."

Asked recently when computers would finally begin to understand human speech, Gates began discussing the critical role of "Bayesian" systems.

Ask any other software executive about anything "Bayesian" and you're liable to get a blank stare.

Is Gates onto something? Is this alien-sounding technology Microsoft's new secret weapon?

Quite possibly.

Bayesian networks are complex diagrams that organize the body of knowledge in any given area by mapping out cause-and-effect relationships among key variables and encoding them with numbers that represent the extent to which one variable is likely to affect another.

Programmed into computers, these systems can automatically generate optimal predictions or decisions even when key pieces of information are missing.

When Microsoft in 1993 hired Eric Horvitz, David Heckerman and Jack Breese, pioneers in the development of Bayesian systems, colleagues in the field were surprised. The field was still an obscure, largely academic enterprise.

Today the field is still obscure. But scratch the surface of a range of new Microsoft products and you're likely to find Bayesian networks embedded in the software. And Bayesian nets are being built into models that are used to predict oil and stock prices, control the space shuttle and diagnose disease.

Artificial intelligence (AI) experts, who saw their field discredited in the early 1980s after promising a wave of "thinking" computers that they ultimately couldn't produce, believe widening acceptance of the Bayesian approach could herald a renaissance in the field.

Bayesian networks provide "an overarching graphical framework" that brings together diverse elements of AI and increases the range of its likely application to the real world, says Michael Jordon, professor of brain and cognitive science at the Massachusetts Institute of Technology.

Microsoft is unquestionably the most aggressive in exploiting the new approach. The company offers a free Web service that helps customers diagnose printing problems with their computers and recommends the quickest way to resolve them. Another Web service helps parents diagnose their children's health problems.

The latest version of Microsoft Office software uses the technology to offer a user help based on past experience, how the mouse is being moved and what task is being done.

"If his actions show he is distracted, he is likely to need help," Horvitz says. "If he's been working on a chart, chances are he needs help formatting the chart."

"Gates likes to talk about how computers are now deaf, dumb, blind and clueless. The Bayesian stuff helps deal with the clueless part," says Daniel T. Ling, director of Microsoft's research division and a former IBM scientist.

Bayesian networks get their name from the Rev. Thomas Bayes, who wrote an essay, posthumously published in 1763, that offered a mathematical formula for calculating probabilities among several variables that are causally related but for which--unlike calculating the probability of a coin landing on heads or tails--the relationships can't easily be derived by experimentation.

Early students of probability applied the ideas to discussions about the existence of God or efforts to improve their odds in gambling. Much later, social scientists used it to help clarify the key factors influencing a particular event.

But it was the rapid progress in computer power and the development of key mathematical equations that made it possible for the first time, in the late 1980s, to compute Bayesian networks with enough variables that they were useful in practical applications.

The Bayesian approach filled a void in the decades-long effort to add intelligence to computers.

In the late 1970s and '80s, reacting to the "brute force" approach to problem solving by early users of computers, proponents of the emerging field of artificial intelligence began developing software programs using rule-based, if-then propositions. But the systems took time to put together and didn't work well if, as was frequently the case, you couldn't answer all the computer's questions clearly.

Later companies began using a technique called "neural nets" in which a computer would be presented with huge amounts of data on a particular problem and programmed to pull out patterns. A computer fed with a big stack of X-rays and told whether or not cancer was present in each case would pick out patterns that would then be used to interpret X-rays.

But the neural nets won't help predict the unforeseen. You can't train a neural net to identify an incoming missile or plane because you could never get sufficient data to train the system.

In part because of these limitations, a slew of companies that popped up in the early 1980s to sell artificial intelligence systems virtually all went bankrupt.

Many AI techniques continued to be used. Credit card companies, for example, began routinely using neural networks to pick out transactions that don't look right based on a consumer's past behavior. But increasingly, AI was regarded as a tool with limited use.

Then, in the late 1980s--spurred by the early work of Judea Pearl, a professor of computer science at UCLA, and breakthrough mathematical equations by Danish researchers -- AI researchers discovered that Bayesian networks offered an efficient way to deal with the lack or ambiguity of information that has hampered previous systems.

Horvitz and his two Microsoft colleagues, who were then classmates at Stanford University, began building Bayesian networks to help diagnose the condition of patients without turning to surgery.

The approach was efficient, says Horvitz, because you could combine historical data, which had been meticulously gathered, with the less precise but more intuitive knowledge of experts on how things work to get the optimal answer given the information available at a given time.

Horvitz, who with two colleagues founded Knowledge Industries to develop tools for developing Bayesian networks, says he and the others left the company to join Microsoft in part because they wanted to see their theoretical work more broadly applied.

Although the company did important work for the National Aeronautics and Space Administration and on medical diagnostics, Horvitz says, "It's not like your grandmother will use it."

Microsoft's activities in the field are now helping to build a groundswell of support for Bayesian ideas.

"People look up to Microsoft," says Pearl, who wrote one of the key early texts on Bayesian networks in 1988 and has become an unofficial spokesman for the field. "They've given a boost to the whole area."

A researcher at German conglomerate Siemens says Microsoft's work has drawn the attention of his superiors, who are now looking seriously at applying Bayesian concepts to a range of industrial applications.

Scott Musman, a computer consultant in Arlington, Va., recently designed a Bayesian network for the Navy that can identify enemy missiles, aircraft or vessels and recommend which weapons could be used most advantageously against incoming targets.

Musman says previous attempts using traditional mathematical approaches on state-of-the-art computers would get the right answer but would take two to three minutes.

"But you only have 30 seconds before the missile has hit you," says Musman.

General Electric is using Bayesian techniques to develop a system that will take information from sensors attached to an engine and, based on expert opinion built into the system as well as vast amounts of data on past engine performance, pinpoint emerging problems.

Microsoft is working on techniques that will enable the Bayesian networks to "learn" or update themselves automatically based on new knowledge, a task that is currently cumbersome.

The company is also working on using Bayesian techniques to improve upon popular AI approaches such as "data mining" and "collaborative filtering" that help draw out relevant pieces of information from massive databases. The latter will be used by Microsoft in its new online entertainment service to help people identify the kind of restaurants or entertainment they are most likely to enjoy.

Still, as effective as they are proving to be in early use, Bayesian networks face an uphill battle in gaining broad acceptance.

"An effective solution came just as the bloom had come off the AI rose," says Peter Hart, head of Ricoh's California Research Center at Menlo Park, a pioneer of AI.

And skeptics insist any computer reasoning system will always fall short of people's expectations because of the computer's tendency to miss what is often obvious to the human expert.

Still, Hart believes the technology will catch on because it is cost-effective. Hart developed a Bayesian-based system that enabled Ricoh's copier help desk to answer twice the number of customer questions in almost half the time.

Hart says Ricoh is now looking at embedding the networks in products so customers can see for themselves what the likely problems are. He believes auto makers will soon build Bayesian nets into cars that predict when various components of a car need to be repaired or replaced.  
"""
print(summarize(text,ratio=0.03).replace("\n","* \n"))
