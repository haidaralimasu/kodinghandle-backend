from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from blog.models import BlogPost
from .models import Comment


class GetBlogCommentsView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, blogSlug, format=None):
        try:
            blog_slug = blogSlug
        except:
            return Response(
                {'error': 'Blog ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            if not BlogPost.objects.filter(slug=blog_slug).exists():
                return Response(
                    {'error': 'This blog does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            blog = BlogPost.objects.get(slug=blog_slug)

            results = []

            if Comment.objects.filter(blog=blog).exists():
                comments = Comment.objects.order_by(
                    '-date_created'
                ).filter(blog=blog)

                for comment in comments:
                    item = {}

                    item['id'] = comment.id
                    item['comment'] = comment.comment
                    item['date_created'] = comment.date_created
                    item['user'] = comment.user.username

                    results.append(item)

            return Response(
                {'comments': results},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving comments'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetBlogCommentView(APIView):
    def get(self, request, blogSlug, format=None):
        user = self.request.user

        try:
            blog_slug = blogSlug
        except:
            return Response(
                {'error': 'Blog ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            if not BlogPost.objects.filter(slug=blog_slug).exists():
                return Response(
                    {'error': 'This Blog does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            blog = BlogPost.objects.get(slug=blog_slug)

            result = {}

            if Comment.objects.filter(user=user, blog=blog).exists():
                comment = Comment.objects.get(user=user, blog=blog)

                result['id'] = comment.id
                result['comment'] = comment.comment
                result['date_created'] = comment.date_created
                result['user'] = comment.user.username

            return Response(
                {'comment': result},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving comment'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CreateBlogCommentView(APIView):
    def post(self, request, blogSlug, format=None):
        user = self.request.user
        data = self.request.data

        try:
            blog_slug = blogSlug
        except:
            return Response(
                {'error': 'blog ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            comment = str(data['comment'])
        except:
            return Response(
                {'error': 'Must pass a comment when creating comment'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if not BlogPost.objects.filter(slug=blog_slug).exists():
                return Response(
                    {'error': 'This blog does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            blog = BlogPost.objects.get(slug=blog_slug)

            result = {}
            results = []

            if Comment.objects.filter(user=user, blog=blog).exists():
                return Response(
                    {'error': 'Blog for this blog already created'},
                    status=status.HTTP_409_CONFLICT
                )

            comment = Comment.objects.create(
                user=user,
                blog=blog,
                comment=comment
            )

            if Comment.objects.filter(user=user, blog=blog).exists():
                result['id'] = comment.id
                result['comment'] = comment.comment
                result['date_created'] = comment.date_created
                result['user'] = comment.user.first_name

                comments = Comment.objects.order_by('-date_created').filter(
                    blog=blog
                )

                for comment in comments:
                    item = {}

                    item['id'] = comment.id
                    item['comment'] = comment.comment
                    item['date_created'] = comment.date_created
                    item['user'] = comment.user.username

                    results.append(item)

            return Response(
                {'comment': result, 'comments': results},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error': 'Something went wrong when creating comment'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
