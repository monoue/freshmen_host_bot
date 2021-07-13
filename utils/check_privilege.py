import config


def executed_by_monoue(author_id) -> bool:
    return author_id == config.MONOUE_ID


def executed_by_staff(author_roles) -> bool:
    for role in author_roles:
        if role.name == "staff":
            return True
    return False


def executed_by_privileged_member(ctx) -> bool:
    author = ctx.author
    return executed_by_monoue(author.id) or executed_by_staff(author.roles)
