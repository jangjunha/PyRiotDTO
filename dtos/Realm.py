class Realm(object):
    """ Realm DTO object

    Attributes:
        lg (string): Legacy script mode for IE6 or older.
        cdn (string): The base CDN url.
        l (string): Default language for this realm.
        n (Map[string, string]): Latest changed version for each data type listed.
        profileiconmax (int): Special behavior number identifying the largest profileicon id that can be used under 500. Any profileicon that is requested between this number and 500 should be mapped to 0.
        css (string): Latest changed version of Dragon Magic's css file.
        v (string): Current version of this file for this realm.
        dd (string): Latest changed version of Dragon Magic.
        store (string): Additional api data drawn from other sources that may be related to data dragon functionality.
    """

    def __init__(self, lg, cdn, l, n, profileiconmax, css, v, dd, store):
        self.lg = lg
        self.cdn = cdn
        self.l = l
        self.n = n
        self.profileiconmax = profileiconmax
        self.css = css
        self.v = v
        self.dd = dd
        self.store = store
