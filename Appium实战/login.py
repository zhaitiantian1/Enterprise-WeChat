from decrator import authicate


def checkuser_logged_in(re):
    if re == "1":
        return True
    elif re == "2":
        return False


@authicate
def post_comment(res):
    print("评论成功+" + res)


if __name__ == '__main__':
    post_comment('1')
# print(result)
