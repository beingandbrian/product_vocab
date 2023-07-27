from db_setup import *

# # instantiating a session to add a row to the db
# with Session() as session:
#     words = session.query(Word).all()
#     creator = Creator(username='creator',first_name='Brian',last_name='Clive',email='bri_cli@gmail.com',password='password')
#     session.add(creator) 
#     session.flush()
#     # word = Word(word_name='prelast', 
#     #     definition='penultimate or the item before the last item in a list', 
#     #     example='Usually chosen last, the boy surprised when the team captain chose him prelast.', 
#     #     creator_id=creator.id,
#     #     creator=creator)
#     # session.add(word)
#     session.commit()
#     # creator = Creator(username='creator',first_name='Brian',last_name='Clive',email='bri_cli@gmail.com',password='password')
    # session.add(creator)
    # session.flush()
    # word = Word(word_name='medior', definition='the level between senior and junior', example='Can you please define the word medior?', creator_id=creator.id)
    # session.add(word)
    # session.commit()
    # word = session.query(Word).filter_by(word_name='tocab').one()
    # print(word.definition)

# with Session() as session:
#     words = session.query(Word).all()
#     for word in words:
#         # print(word.creator_id)
#         creator = session.query(Creator).filter_by(id=word.creator_id).one()
#         word.creator = creator
#         session.add(word)
#     session.commit()
# print([word.creator.get_creator_name() for word in words])
