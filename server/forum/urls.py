from rest_framework import routers

from .viewsets import PostViewSet, CommentViewSet, TopicViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('topics', TopicViewSet)

urlpatterns = router.urls