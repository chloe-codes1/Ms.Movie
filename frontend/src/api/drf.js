// drf.js 를 import 하면 아래의 코드를 object로 받게 하기
export default{
    URL: 'http://localhost:8000', // **잊지마! 배포 시 바꿔야 할 것!!**
    ROUTES: {
        signup: '/rest-auth/signup/',
        login: '/rest-auth/login/',
        logout: '/rest-auth/logout/',
        profile: '/accounts/profile/',
        othersProfile: '/accounts/',
        movieList: '/movies/',
        movieRecommendation: '/movies/recommendation/',
        movieDetail: '/movies/:id/',
        reviewList: '/reviews/:id/',
        reviewDetail: '/reviews/detail/:id',
        commentCreate: '/reviews/:id/comments/',
        commentDetail: '/reviews/:reviewId/comments/:commentId',
        reviewLike: '/reviews/:id/like/',
        reviewDislike: '/reviews/:id/dislike/',
    }
}