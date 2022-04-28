from db_setup import *

with Session() as session:
    # creator = Creator(username='creator',first_name='Stevening',last_name='Evening',email='an_email@gmail.com',password='password')
    # session.add(creator)
    # session.flush()
    # word = Word(word_name='tocab', definition='test vocab', example='Can you create some tocab for the software?', creator_id=creator.id)
    # session.add(word)
    # session.commit()
    word = session.query(Word).filter_by(word_name='tocab').one()
    print(word.definition)

# with session_manager() as session:
#     # creator = Creator(username='creator',first_name='Stevening',last_name='Evening',email='an_email@gmail.com',password='password')
#     # session.add(creator)
#     # session.flush()
#     # word = Word(word_name='tocab', definition='test vocab', example='Can you create some tocab for the software?', creator_id=creator.id)
#     # session.add(word)
#     # session.commit()
#     word = session.query(Word).filter_by(word_name='tocab').one()
#     print(word.definition)