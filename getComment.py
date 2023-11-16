from youtube_comment_downloader import *

class YtComments:

    def GetComments(self,url):
        downloader = YoutubeCommentDownloader()
        comments = downloader.get_comments_from_url(url, sort_by=SORT_BY_POPULAR)
    
        return comments

    
if __name__ == "__main__":
    comm = YtComments()
    comm.GetComments("https://www.youtube.com/watch?v=eIoQy-JeU7M&ab_channel=CiccioGamer89")