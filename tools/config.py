# Cấu hình site rv (Sổ tay đánh giá laptop). URL gốc chỉ nằm trong file này.
BASE_URL = "https://danhgia-laptop-vn.github.io/"
SITE_NAME = "Sổ tay đánh giá laptop"
PEN = "Khoa"
MARK = "R"
AVATAR = "K"
TAGLINE = "Ghi chép của Khoa"
LATEST_N = 12

INDEX_TITLE = "Sổ tay đánh giá laptop - Ghi chép đọc thông số và kết quả đo"
INDEX_DESC = ("Ghi chép cách đọc đánh giá laptop đời 2025 và 2026: webcam, micro, chip phổ thông, máy tân trang. "
              "Mỗi bài có bảng đối chiếu và lưu ý khi chọn máy.")
INDEX_OG_TITLE = INDEX_TITLE
INDEX_OG_DESC = INDEX_DESC
INDEX_H1 = "Đọc đánh giá laptop sao cho đỡ nhầm"
STRAP = "Mình ghi lại cách đọc thông số, kết quả đo và điều kiện bảo hành của laptop đời 2025 và 2026."

ABOUT_P = "Mình ghi lại cách đọc đánh giá laptop, kèm bảng đối chiếu cho máy đời 2025 và 2026."
ABOUT_HOME = (
    '<h2 class="sec-t">Về blog</h2>'
    '<p>Mình là Khoa. Blog này là sổ tay của mình về chuyện đọc đánh giá laptop: webcam và micro khi họp, '
    'chip phổ thông, máy tân trang và giấy tờ đi kèm.</p>'
    '<p>Mỗi bài mình viết theo một câu hỏi cụ thể, rồi gom thông số vào bảng để so từng dòng. '
    'Mình chỉ nhắc đến máy đời 2025 và 2026 và không ghi giá, vì giá đổi theo từng tuần.</p>'
    '<p>Các bài đều có phần lưu ý cuối cùng, nơi mình ghi những chỗ dễ bị đọc nhầm khi xem thông số.</p>'
)

CATS = [("hop", "Họp và làm việc"), ("chip", "Chip và thông số"), ("may-cu", "Máy tân trang")]
CAT_RULES = [
    ("hop", "Họp và làm việc", ["webcam", "micro", "hop"]),
    ("may-cu", "Máy tân trang", ["tan-trang", "bao-hanh", "serial"]),
    ("chip", "Chip và thông số", ["chip", "core", "ryzen", "cpu"]),
]
CAT_DEFAULT = ("chip", "Chip và thông số")

FONTS_URL = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"

HEADER = (
    '<body>\n<a class="skip" href="#main">Bỏ qua đến nội dung</a>\n'
    '<header class="top"><div class="wrap bar">'
    '<a class="brand" href="@HOME@"><span class="mark" aria-hidden="true">@MARK@</span>'
    '<span class="bn"><b>@NAME@</b><small>@TAGLINE@</small></span></a>'
    '<nav class="nav" aria-label="Chính">@NAV@</nav>'
    '</div></header>\n'
)
FOOTER = (
    '<footer class="foot"><div class="wrap fo">'
    '<p><b>@NAME@</b>, blog cá nhân của @PEN@. Ghi chép đọc đánh giá laptop đời 2025 và 2026.</p>'
    '<p class="sm">Nội dung viết lại từ tài liệu và kết quả đo công khai. Năm @YEAR@.</p>'
    '</div></footer>\n</body>\n</html>\n'
)
ABOUT = (
    '<section class="w w-about"><span class="av" aria-hidden="true">@AV@</span>'
    '<div><h2 class="w-t">@PEN@</h2><p>@ABOUT@</p><a class="more" href="@R@#ve-blog">Về blog</a></div></section>'
)
POST = (
    '@HEADER@'
    '<div class="wrap lay"><main id="main" class="col post">\n'
    '<p class="crumb"><a href="@R@">Trang chủ</a><span aria-hidden="true"> / </span><span>@CATLABEL@</span></p>\n'
    '@ARTICLE@\n@RELATED@\n</main>\n'
    '<aside class="side">@ABOUT@@CATS@</aside></div>\n'
    '@FOOTER@'
)
INDEX = (
    '@HEADER@'
    '<main id="main">\n'
    '<div class="wrap intro"><h1>@H1@</h1><p>@STRAP@</p></div>\n'
    '<div class="wrap"><section class="hero-wrap" aria-label="Bài mới nhất">@HERO@</section></div>\n'
    '<div class="wrap lay"><div class="col">\n'
    '<section id="bai-moi"><h2 class="sec-t">Bài mới nhất</h2>\n<div class="grid">\n@LATEST@\n</div></section>\n'
    '<section id="chu-de"><h2 class="sec-t">Theo chủ đề</h2>\n<div class="tps">@TOPICS@</div></section>\n'
    '<section id="ve-blog" class="about-home">@ABOUT_HOME@</section>\n'
    '</div>\n<aside class="side">@SIDEBAR@</aside></div>\n</main>\n'
    '@FOOTER@'
)
NOTFOUND = (
    '@HEADER@'
    '<main id="main" class="wrap nf"><h1>Không tìm thấy trang này</h1>'
    '<p>Đường dẫn có thể đã đổi hoặc bài chưa được đăng. Quay về trang chủ để xem danh sách bài.</p>'
    '<p><a class="btn" href="@R@">Về trang chủ</a></p></main>\n'
    '@FOOTER@'
)
CARDS = {
    "hero": (
        '<article class="hero"><a class="hero-media" href="@HREF@" tabindex="-1" aria-hidden="true">@MEDIA@</a>'
        '<div class="hero-tx"><span class="badge">@CAT@</span>'
        '<h2><a href="@HREF@">@TITLE@</a></h2><p>@DESC@</p>'
        '<p class="meta"><time datetime="@ISO@">@DATE@</time><span aria-hidden="true"> · </span>@READ@</p>'
        '<a class="btn" href="@HREF@">Đọc bài</a></div></article>'
    ),
    "latest": (
        '<article class="card"><a class="card-media" href="@HREF@" tabindex="-1" aria-hidden="true">@MEDIA@</a>'
        '<div class="card-tx"><span class="badge">@CAT@</span>'
        '<h3><a href="@HREF@">@TITLE@</a></h3><p>@DESC@</p>'
        '<p class="meta"><time datetime="@ISO@">@DATE@</time><span aria-hidden="true"> · </span>@READ@</p></div></article>'
    ),
}
