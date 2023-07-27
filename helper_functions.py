def check_un_and_email(form_un, form_email):
    with Session() as session:
        creator = session.query(Creator).filter(or_(Creator.username==form_un, Creator.email==form_email)).one()
    return True if creator else False
