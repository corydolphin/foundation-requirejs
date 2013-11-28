#
# @author Cory Dolphin
# @wcdolphin
#

from goodmeme import app, db
import datetime
import goodmeme.utils
import re
import shortuuid


class Meme(db.Document):
    top_line = db.StringField(max_length=255, required=True)
    bottom_line = db.StringField(max_length=255, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    meme_type  = db.ObjectIdField(default=None, required=False)

    @property
    def s3_path(self):
        return "%s/%s.jpg" % ("u", self.id)

    @property
    def url(self, scheme=""):
        return "%s%s/%s/%s.jpg" % (scheme, app.config["S3_MEME_URL"], "u", self.id)

    @property
    def view_url(self, scheme="http://"):
        return "%s%s/%s/%s" % (scheme, app.config["ROOT_DOMAIN"], "meme", self.id)

    @property
    def dict(self):
        return {
            'id'          : '%s' % self.id,
            'top_line'    : self.top_line,
            'bottom_line' : self.bottom_line,
            'created_at'  : self.created_at,
            'meme_type'   : '%s' % self.meme_type
        }

    @property
    def has_stock_meme(self):
        return hasattr(self, 'meme_type') and self.meme_type is not None

    @property
    def stock_meme(self):
        if not hasattr(self, 'meme_type') or self.meme_type is None:
            return None
        return StockMeme.objects.get(id=self.meme_type)

class StockMeme(db.Document):
    filename = db.StringField(required=True)
    description = db.StringField(max_length=255, required=True)

    @property
    def dict(self):
        return {
            'filename'          : '%s' % self.filename,
            'description'       : '%s' % self.description,
        }