#!/usr/bin/env python3
"""Builds the static site pages from shared header/footer. Run: python3 _build.py
(Only needed when you change the nav/footer in one place; the generated HTML is committed.)"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
FONTS = (ROOT / '_fonts.txt').read_text().strip()
# The home page's content is read back from index.html itself, so you can edit index.html directly
# and re-running this script only refreshes the nav, footer and post cards.
_idx = (ROOT / 'index.html').read_text()
HOME_BODY = re.search(r'(<main id="top">.*</main>)', _idx, re.S).group(1)

def nav(r):
    return f'''<header>
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="{r}index.html">engage<em>.</em><span>digital learning</span></a>
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul id="menu">
      <li><a href="{r}index.html#book">Book</a></li>
      <li><a href="{r}index.html#framework">Framework</a></li>
      <li><a href="{r}index.html#inside">Chapters</a></li>
      <li><a href="{r}index.html#infographics">Infographics</a></li>
      <li><a href="{r}index.html#author">Author</a></li>
      <li><a href="{r}blog/">AI &amp; Education</a></li>
      <li><a href="{r}index.html#contact">Contact</a></li>
      <li><a class="buy" href="https://www.routledge.com/Designing-Socially-Dynamic-Digital-Learning-Technologies-and-Strategies-for-Student-Engagement/Ou/p/book/9781032436012" target="_blank" rel="noopener">Get the book</a></li>
    </ul>
  </nav>
</header>'''

def footer(r):
    return f'''<footer>
  <div class="wrap">
    <span>© 2024–2026 Chaohua Ou · Engage Digital Learning</span>
    <span><a href="{r}index.html#book">Book</a> · <a href="{r}index.html#author">Author</a> · <a href="{r}blog/">AI &amp; Education</a> · <a href="{r}index.html#contact">Contact</a></span>
  </div>
</footer>'''

SITE = 'https://engagedigitallearning.com'
SITE_NAME = 'Engage Digital Learning'
AUTHOR = 'Chaohua Ou'
BOOK_TITLE = 'Designing Socially Dynamic Digital Learning'
BOOK_SUBTITLE = 'Technologies and Strategies for Student Engagement'
BOOK_URL = 'https://www.routledge.com/Designing-Socially-Dynamic-Digital-Learning-Technologies-and-Strategies-for-Student-Engagement/Ou/p/book/9781032436012'
BOOK_ISBN = '9781032436012'

PERSON_LD = {
  '@type': 'Person', '@id': f'{SITE}/#author', 'name': AUTHOR, 'url': f'{SITE}/#author',
  'image': f'{SITE}/images/chaohua-ou.jpg',
  'jobTitle': 'Director of Data and Learning Technologies',
  'worksFor': {'@type': 'Organization', 'name': 'Lastinger Center for Learning, University of Florida', 'url': 'https://lastinger.center.ufl.edu/'},
  'knowsAbout': ['online learning', 'instructional design', 'student engagement', 'educational technology', 'AI in education', 'peer assessment'],
}

def jsonld(data):
    import json
    return '\n<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', **data}, ensure_ascii=False, indent=1) + '</script>'

def shell(r, title, desc, body, canonical, og_image=None, extra_head='', og_image_alt=None, published=None, modified=None):
    is_article = '/blog/' in canonical and canonical.rstrip('/').split('/')[-1] != 'blog'
    og_image = og_image or 'book-cover.jpg'
    og = f'\n<meta property="og:image" content="{SITE}/images/{og_image}">'
    if og_image_alt: og += f'\n<meta property="og:image:alt" content="{og_image_alt}">'
    if is_article:
        og += f'\n<meta property="article:published_time" content="{published}">'
        if modified: og += f'\n<meta property="article:modified_time" content="{modified}">'
        og += f'\n<meta property="article:author" content="{AUTHOR}">\n<meta property="article:section" content="AI &amp; Education">'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{AUTHOR}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{'article' if is_article else 'website'}">{og}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/images/{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{r}assets/site.css">{extra_head}
</head>
<body>

{nav(r)}

{body}

{footer(r)}

<script src="{r}assets/site.js"></script>
</body>
</html>
'''

# ---------- posts ----------
POSTS = [
  dict(
    slug='designing-ai-augmented-peer-assessment',
    title='Designing AI-Augmented Peer Assessment',
    deck='What did 1,451 students teach us about peer assessment, and what\'s next with AI?',
    date='2025-10-23', date_text='October 23, 2025', read='8 min read',
    image='ai-augmented-peer-assessment.png',
    image_alt='Seven elements of AI-augmented peer assessment arranged across pre-, during- and post-assessment stages',
    summary='Discussion boards scale, but participation is uneven. A five-year study of 1,451 students compared peer assessment with online discussion, and the results point to a design where AI supports every stage of peer review.',
    body='''
<h2>The big picture</h2>
<p>If you've ever taught a large online course, you know the drill: online discussion boards become your go-to tool for student engagement. They're scalable, easy to set up, and research tells us they work. But let's be honest, they also come with their share of headaches: low participation, uneven contributions, or students going through the motions just to check a box.</p>
<p>So, is there a better, or at least complementary, way to drive deeper engagement and learning?</p>
<p>I explored this question with my colleague <a href="https://www.davidjoyner.net/" target="_blank" rel="noopener">David Joyner</a> in a recent large-scale study comparing the effects of peer assessment and online discussion on online students' learning. We analyzed data from 1,451 students in the same online graduate course over five years (Spring 2020 to Fall 2024). What we discovered has really shed light on how we think about strategies for student engagement.</p>

<h2>What did we learn?</h2>
<div class="callouts">
  <div class="callout">
    <h3>Peer assessment is a performance driver</h3>
    <p>Students who actively gave feedback to their peers (we called them "Collaborators" and "Reviewers") significantly outperformed those who mainly stuck to discussion boards ("Discussants") or barely participated at all ("Limited Contributors"). The takeaway? When students critically evaluate their peers' work and provide structured feedback, their own learning takes a serious leap forward (Figure 1).</p>
  </div>
  <div class="callout">
    <h3>Online discussion still matters</h3>
    <p>But before we write off discussion boards entirely, here's the plot twist: our "Discussants" did significantly better than students with minimal engagement. Discussion boards aren't the problem; they're just not the <em>whole</em> solution.</p>
  </div>
  <div class="callout">
    <h3>Peer assessment was a much stronger predictor of both perceived peer support and overall course satisfaction</h3>
    <p>Students didn't just perform better. They <em>felt</em> more supported and valued the course more highly when peer assessment was part of their experience (Figure 2).</p>
  </div>
</div>

<figure class="fig">
  <img loading="lazy" src="../../images/peer-assessment-figure-1.png" alt="Bar chart of mean learning performance by participation group: Collaborators and Reviewers highest, Discussants in the middle, Limited Contributors lowest">
  <figcaption><strong>Figure 1: Mean learning performance scores by student participation group.</strong> The data shows a clear "step-up" effect. Students who actively provided feedback to peers (Collaborators and Reviewers) achieved the highest learning outcomes; students who primarily stuck to discussion boards (Discussants) performed well, but significantly lower than those who engaged in peer review; students with minimal engagement in either activity (Limited Contributors) saw the lowest performance scores.</figcaption>
</figure>

<figure class="fig">
  <img loading="lazy" src="../../images/peer-assessment-figure-2.jpg" alt="Bar chart of standardized coefficients: peer assessment predicts peer support and course effectiveness more strongly than online discussion">
  <figcaption><strong>Figure 2: The hidden value of peer assessment.</strong> This figure measures student sentiment: how much support they felt and how highly they rated the course. We used standardized coefficients (β) to compare the impact of different activities. In plain English, peer assessment is a much stronger predictor of student satisfaction than discussion boards. Even though discussion boards are often used to build community, the act of giving and receiving structured feedback does a better job of making students feel supported by their peers.</figcaption>
</figure>

<h2>What does this mean for teaching?</h2>
<blockquote class="pull">Online discussions are the warm-up, and peer assessment is the workout. Combined strategically, they create a learning rhythm that helps students move from participation to transformation.</blockquote>
<p>Think of it this way: online discussions are like the warm-up. They loosen things up, get students talking, and build comfort. Peer assessment is the workout. It stretches their thinking, builds intellectual stamina, and strengthens their ability to evaluate and reflect. You need both to build learning muscles that last.</p>
<p>When you combine them strategically, you're creating a learning rhythm: online discussions offer easy entry points, while peer assessment provides structured, reflective engagement. Together, they help students move from participation to transformation.</p>

<h2>But here are the challenges</h2>
<p>Anyone who's implemented peer assessment knows it's not exactly plug-and-play. You've got to:</p>
<ul>
  <li>Design clear rubrics (which takes time to create and refine)</li>
  <li>Train students to give quality feedback (not just "Great job!")</li>
  <li>Manage the logistics (who reviews whom? when? how many?)</li>
  <li>Deal with fairness concerns (Is this grade reliable? Is there bias?)</li>
</ul>
<p>These challenges are exactly why many instructors stick with online discussions despite peer assessment's proven benefits. It's just… <em>a lot</em>.</p>

<h2>Enter AI: a game-changer?</h2>
<p>This is where things get exciting (and a bit futuristic). What if AI could tackle those persistent pain points? Not replace the instructor or eliminate the human element, but handle the heavy lifting so we can focus on what matters most: student learning.</p>
<p>Based on my research and emerging work in this space, I've been developing a framework for designing AI-augmented peer assessment. This framework includes seven elements organized across three stages of the peer assessment process. It aims at leveraging AI to streamline logistics, enhance quality feedback, ensure fairness, and ultimately create a richer and more engaging learning experience for all learners.</p>

<figure class="fig">
  <img loading="lazy" src="../../images/ai-augmented-peer-assessment.png" alt="Circular diagram of seven AI-augmented peer assessment elements grouped into pre-assessment, during assessment and post-assessment">
  <figcaption>The framework: seven elements across three stages of peer assessment.</figcaption>
</figure>

<h2>The framework: 7 ways AI could transform peer assessment</h2>

<h3>Pre-assessment: before students start reviewing</h3>
<ol class="steps">
  <li><strong>AI-assisted rubric design.</strong> Imagine typing in your learning objectives and having AI generate a solid first draft of your rubric: clear criteria, performance levels, the works. You review it, tweak it, maybe even involve students in refining it. What used to take hours now takes minutes.</li>
  <li><strong>Intelligent reviewer assignment.</strong> Instead of randomly assigning reviewers (or spending an hour manually matching students), AI does the heavy lifting. It considers who has relevant expertise, balances workloads, avoids conflicts of interest, and even ensures students get diverse perspectives. Smart matching, zero headache.</li>
  <li><strong>Personalized feedback coaching.</strong> Before students review their peers' actual work, AI trains them. They practice on sample submissions, get immediate feedback on their comments ("This is too vague. Can you be more specific?"), and build their skills progressively. By the time they're reviewing real work, they know what good feedback looks like.</li>
</ol>

<h3>During assessment: while students are reviewing</h3>
<ol class="steps" start="4">
  <li><strong>AI feedback validation.</strong> As students write their peer reviews, AI acts like a real-time coach. "Your comment is constructive, but could you add a specific example?" or "You've addressed criterion #1 well, but what about criterion #2?" It catches issues before feedback gets submitted, ensuring quality and relevance.</li>
  <li><strong>Automated review oversight.</strong> Here's where AI becomes your teaching assistant. It monitors all reviews for quality, spots potential bias, flags suspiciously similar feedback (collusion, anyone?), and alerts you to cases that need your attention. You're not drowning in data. Instead, you're getting actionable insights about where to focus your limited time.</li>
</ol>

<h3>Post-assessment: after reviews are completed</h3>
<ol class="steps" start="6">
  <li><strong>AI-supported feedback synthesis.</strong> Students receive feedback from multiple peers: some helpful, some redundant, some contradictory. AI synthesizes it all into a coherent summary: "Here are the common themes, here's where reviewers agreed, here's where they diverged, and here are your top three priorities for revision." Clear, actionable, not overwhelming.</li>
  <li><strong>Analytics-driven interventions.</strong> AI analyzes patterns across all the peer assessment data. Which students are struggling? What common misconceptions keep appearing? Which rubric criteria are confusing? You get dashboards and insights that help you intervene early and refine your teaching. It's evidence-based decision-making on steroids.</li>
</ol>

<figure class="fig tall">
  <img loading="lazy" src="../../images/7-ways-ai-could-transform-peer-assessment.png" alt="Infographic: 7 ways AI could transform peer assessment">
  <figcaption>7 ways AI could transform peer assessment (infographic).</figcaption>
</figure>

<h2>The reality check</h2>
<p>Now, before you get too excited (or worried), let me be clear: some of these elements exist in various tools today. Others are still in the research phase. Building a comprehensive platform that does all seven seamlessly? That's going to take serious development work, cross-disciplinary collaboration, and significant investment.</p>
<p>More importantly, we need to proceed thoughtfully. As we build these AI-powered solutions, we have to grapple with some hard questions:</p>
<ul>
  <li>How do we protect student privacy while using their data to improve learning?</li>
  <li>How do we ensure AI doesn't perpetuate or amplify bias?</li>
  <li>How do we maintain transparency so students and instructors understand how AI is making decisions?</li>
  <li>Where's the line between helpful automation and over-reliance on algorithms?</li>
</ul>
<p>The goal isn't to replace instructors or eliminate human judgment. It's to free us from the logistical nightmare so we can focus on what we do best: teaching, mentoring, and making thoughtful pedagogical decisions.</p>
<p>We're not there yet. But with thoughtful development, ethical consideration, and continued research, I think we can get there.</p>
<p>What do you think? I'd love to hear your experiences with peer assessment: the good, the bad, and the "never again."</p>

<h2>Want to dive deeper?</h2>
<p>If you are interested in the research behind this framework, here are some excellent resources:</p>
<ol class="refs">
  <li>Darvishi, A., Khosravi, H., Sadiq, S., &amp; Gašević, D. (2022). Incorporating AI and learning analytics to build trustworthy peer assessment systems. <em>British Journal of Educational Technology, 53</em>(4), 844–875. <a href="https://doi.org/10.1111/bjet.13233">https://doi.org/10.1111/bjet.13233</a></li>
  <li>Ou, C. (2024). Engaging students with peer assessment. In C. Ou, <em>Designing Socially Dynamic Digital Learning</em> (pp. 98–112). Routledge. <a href="https://doi.org/10.4324/9781003368076">https://doi.org/10.4324/9781003368076</a></li>
  <li>Ou, C., &amp; Joyner, D. A. (2025). Assess or discuss: Comparing peer assessment and online discussion for enhancing learning at scale. <em>L@S '25: Proceedings of the Twelfth ACM Conference on Learning @ Scale</em>, 222–226. <a href="https://doi.org/10.1145/3698205.3733927">https://doi.org/10.1145/3698205.3733927</a></li>
  <li>Ou, C., Thajchayapong, P., &amp; Joyner, D. A. (2024). Open, collaborative, and AI-augmented peer assessment: Student participation, performance, and perceptions. <em>L@S '24: Proceedings of the Eleventh ACM Conference on Learning @ Scale</em>, 496–500. <a href="https://doi.org/10.1145/3657604.3664705">https://doi.org/10.1145/3657604.3664705</a></li>
  <li>Sichterman, B., Noroozi, O., Boetje, J., van Ginkel, S., Khosravi, H., &amp; Versendaal, J. (2025). Supporting peer learning with artificial intelligence: A systematic literature review. <em>Innovations in Education and Teaching International, 62</em>(5), 1648–1664. <a href="https://doi.org/10.1080/14703297.2025.2530118">https://doi.org/10.1080/14703297.2025.2530118</a></li>
  <li>Topping, K. J., Gehringer, E., Khosravi, H., Gudipati, S., Jadhav, K., &amp; Susarla, S. (2025). Enhancing peer assessment with artificial intelligence. <em>International Journal of Educational Technology in Higher Education, 22</em>(1). <a href="https://doi.org/10.1186/s41239-024-00501-1">https://doi.org/10.1186/s41239-024-00501-1</a></li>
</ol>

<div class="cite">
  <p class="eyebrow">How to cite this post</p>
  <p>Ou, C. (2025, October 23). <em>Designing AI-augmented peer assessment</em>. https://engagedigitallearning.com/blog/designing-ai-augmented-peer-assessment/</p>
</div>
'''),
  dict(
    slug='ai-fluency-framework',
    title='An AI Fluency Framework',
    deck='Inspired by the dual role of AI in online project-based learning.',
    date='2025-07-22', date_text='July 22, 2025', read='5 min read',
    image='ai-fluency-framework.png',
    image_alt='AI Fluency Framework: three overlapping circles for learning with AI, learning about AI and learning through AI creation, with AI skills, AI knowledge and AI creation around them',
    summary='Students in a six-semester online graduate course weren\'t only using AI; they were building with it. A paper with David Joyner at ACM Learning @ Scale describes this dual role and a framework for AI fluency.',
    body='''
<p>A paper I co-authored with <a href="https://www.davidjoyner.net/" target="_blank" rel="noopener">David Joyner</a>, <a href="https://dl.acm.org/doi/abs/10.1145/3698205.3733950" target="_blank" rel="noopener">The Dual Role of AI in Online Project-Based Learning at Scale</a>, just came out in the ACM Learning @ Scale conference proceedings, and I wanted to give you a quick peek at what we discovered.</p>

<h2>The big picture</h2>
<p>There have been a lot of discussions on <em>learning about AI</em> and <em>learning with AI</em>. What caught our attention was something different: students weren't just using AI, they were creating with it in their course projects. This led us to explore what we call the "dual role" of AI in project-based learning.</p>
<p>We analyzed student projects and course survey data collected from an online graduate course on educational technology over six semesters (2023–2024). Students worked on a semester-long project in one of three tracks: Research, Education, or Development. What we found was pretty remarkable: students were engaging with AI in two distinct ways that complemented each other beautifully.</p>
<figure class="fig">
  <img loading="lazy" src="../../images/dual-role-method.png" alt="Study method: student projects and survey data from six semesters across Research, Education and Development tracks">
  <figcaption>Study design: projects and survey data from six semesters, three project tracks.</figcaption>
</figure>

<h2>AI as learning assistant</h2>
<p>First, there's AI as a learning assistant. About three-quarters of the students used AI to support their project-based learning in various ways: assisting in technical tasks, research and exploration, content generation and editing, brainstorming and ideation, and project feedback. Interestingly, some used ChatGPT as a "therapist" for stress management during intense project phases. Others used AI to generate alt-text for accessibility or create voice-overs for their presentations. One student even used AI as a simulated interview subject for their research!</p>
<blockquote class="pull">Students used AI to support project-based learning in various ways.</blockquote>
<figure class="fig">
  <img loading="lazy" src="../../images/ai-tool-usage.png" alt="Chart of how students used AI tools in their projects: technical tasks, research, content generation, brainstorming, feedback">
  <figcaption>How students used AI as a learning assistant.</figcaption>
</figure>

<h2>AI as creation medium</h2>
<p>Here's where it gets really interesting. When we analyzed what students were actually building for their projects, AI in Education emerged as the most popular theme, appearing in nearly one-third of all projects (32.3%). Within the 141 projects focused on AI in Education, we identified distinct subthemes representing different approaches to AI integration. The variety was impressive.</p>
<blockquote class="pull">Students weren't just using AI. They were creating AI-driven educational tools.</blockquote>
<figure class="fig">
  <img loading="lazy" src="../../images/ai-projects.png" alt="Chart of AI in Education project subthemes among 141 student projects">
  <figcaption>Subthemes among the 141 AI in Education projects.</figcaption>
</figure>

<h2>What does this mean?</h2>
<p>The dual role we observed suggests something important: students are not just consumers of AI technologies. They're transitioning from AI users to AI creators.</p>
<p>This has real implications for how we design educational experiences. Instead of choosing between "teaching about AI" or "using AI tools," we can do both simultaneously through well-designed project-based learning environments.</p>

<h2>The bigger questions</h2>
<p>Our research also highlighted some areas that deserve more attention. While students showed strong interest in AI ethics (8.5% of AI projects), we'd love to see even more emphasis on responsible AI development. Similarly, AI for accessibility represented only 2.1% of projects, a missed opportunity given AI's potential to make education more inclusive.</p>

<h2>What's next?</h2>
<p>This study gives us a snapshot of how graduate students engage with AI in project-based learning, but it raises so many more questions. How do these experiences shape students' long-term attitudes toward AI? What happens when we apply these approaches in different disciplines or with different student populations? How can we better scaffold the transition from AI user to AI creator?</p>

<h2>An AI Fluency Framework</h2>
<p>To me, the dual role of AI calls for a broader definition of AI fluency, one that encompasses not only how students use AI tools but also how they build knowledge of AI and create with it.</p>
<p>That reflection led me to develop the following AI Fluency Framework, which illustrates three interwoven dimensions of learning:</p>
<ul>
  <li><strong>AI Knowledge</strong>: understanding how AI works, its applications, ethics, and social impact</li>
  <li><strong>AI Skills</strong>: using AI tools productively for learning, research, and creativity</li>
  <li><strong>AI Creation</strong>: designing, building, and reflecting on AI-driven solutions</li>
</ul>
<p>I hope this model offers a helpful lens for educators, designers, and researchers exploring AI literacy and fluency.</p>
<figure class="fig">
  <img loading="lazy" src="../../images/ai-fluency-framework.png" alt="AI Fluency Framework diagram: learning with AI, learning about AI, and learning through AI creation, surrounded by AI skills, AI knowledge, AI creation and guiding questions">
  <figcaption>The AI Fluency Framework.</figcaption>
</figure>

<h2>Want to dive deeper?</h2>
<ul class="refs">
  <li><a href="https://doi.org/10.1145/3698205.3733950">Read the full paper</a> for the methodology, detailed results, and implications for curriculum design.</li>
  <li>Check out an earlier paper, <a href="https://onlineinnovationsjournal.com/streams/scholarship-of-online-teaching-and-learning/558e61304d6df55a.html">Seven Years of Online Project-Based Learning at Scale</a>, if you are interested in how this course was designed as a model of online project-based learning at scale.</li>
  <li>Still interested? See the book, <a href="../../index.html">Designing Socially Dynamic Digital Learning</a>, for technologies and strategies for engaging students with online project-based learning.</li>
</ul>

<div class="cite">
  <p class="eyebrow">How to cite this post</p>
  <p>Ou, C. (2025, July 22). <em>An AI Fluency Framework</em>. https://engagedigitallearning.com/blog/ai-fluency-framework/</p>
</div>
'''),
]

def post_card(p, r):
    return f'''<article class="post">
  <a class="img" href="{r}blog/{p['slug']}/"><img loading="lazy" src="{r}images/{p['image']}" alt="{p['image_alt']}"></a>
  <time datetime="{p['date']}">{p['date_text']}</time>
  <h3><a href="{r}blog/{p['slug']}/">{p['title']}</a></h3>
  <p>{p['summary']}</p>
  <a class="more" href="{r}blog/{p['slug']}/">Read the post →</a>
</article>'''

def build_post(p, other):
    r = '../../'
    body = f'''<main id="top">
<section class="hero post-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="{r}blog/">AI &amp; Education</a> · <time datetime="{p['date']}">{p['date_text']}</time> · {p['read']}</p>
    <h1>{p['title']}</h1>
    <p class="deck">{p['deck']}</p>
    <p class="by">By <b>Chaohua Ou</b></p>
  </div>
</section>

<article class="post-body">
  <div class="wrap">
    <div class="prose">
{p['body']}
    </div>
  </div>
</article>

<section class="band more-writing">
  <div class="wrap">
    <p class="eyebrow">More writing</p>
    <div class="posts">
{post_card(other, r)}
    </div>
    <p style="margin-top:2rem"><a class="btn" href="{r}blog/">All posts</a> <a class="btn ghost" href="{r}index.html#book" style="margin-left:.5rem">About the book</a></p>
  </div>
</section>
</main>'''
    url = f"{SITE}/blog/{p['slug']}/"
    ld = jsonld({
      '@type': 'BlogPosting', '@id': url, 'mainEntityOfPage': url, 'url': url,
      'headline': p['title'], 'alternativeHeadline': p['deck'], 'description': p['summary'],
      'image': {'@type': 'ImageObject', 'url': f"{SITE}/images/{p['image']}", 'caption': p['image_alt']},
      'datePublished': p['date'], 'dateModified': p.get('modified', p['date']),
      'author': PERSON_LD, 'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE + '/', 'logo': {'@type': 'ImageObject', 'url': f'{SITE}/images/book-cover.jpg'}},
      'inLanguage': 'en-US', 'isPartOf': {'@type': 'Blog', '@id': f'{SITE}/blog/#blog', 'name': 'AI & Education'},
      'keywords': p.get('keywords', ['AI in education', 'online learning', 'student engagement']),
      'isAccessibleForFree': True,
    })
    return shell(r, f"{p['title']} · {SITE_NAME}", p['summary'].replace('"','&quot;'), body,
                 url, p['image'], extra_head=ld, og_image_alt=p['image_alt'].replace('"','&quot;'),
                 published=p['date'], modified=p.get('modified'))

def build_blog_index():
    r = '../'
    cards = '\n'.join(post_card(p, r) for p in POSTS)
    body = f'''<main id="top">
<section class="hero post-hero">
  <div class="wrap">
    <p class="eyebrow">AI &amp; Education</p>
    <h1>Notes from the Intersection of AI and Education</h1>
    <p class="deck">Evolving thoughts and experiences with AI in education: what I'm learning, experimenting with, and questioning along the way, one idea and reflection at a time.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="posts">
{cards}
    </div>
  </div>
</section>
</main>'''
    ld = jsonld({
      '@type': 'Blog', '@id': f'{SITE}/blog/#blog', 'url': f'{SITE}/blog/', 'name': 'AI & Education',
      'description': 'Writing by Chaohua Ou on AI, student engagement and digital learning design.',
      'author': PERSON_LD, 'inLanguage': 'en-US',
      'blogPost': [{'@type': 'BlogPosting', '@id': f"{SITE}/blog/{p['slug']}/", 'url': f"{SITE}/blog/{p['slug']}/", 'headline': p['title'], 'datePublished': p['date'], 'image': f"{SITE}/images/{p['image']}"} for p in POSTS],
    })
    return shell(r, f'AI &amp; Education: Notes on AI, Teaching and Learning · {SITE_NAME}',
                 'Essays by Chaohua Ou on AI in education, peer assessment, project-based learning, student engagement and online course design.',
                 body, f'{SITE}/blog/', extra_head=ld)

def build_home():
    body = HOME_BODY + '''

<div class="lightbox" id="lightbox" hidden>
  <button type="button" id="lbClose" aria-label="Close">×</button>
  <img id="lbImg" src="" alt="">
</div>'''
    # swap the home page's inline post cards for generated ones (keeps them in sync with the posts)
    start = body.index('<div class="posts">'); end = body.index('</div>\n  </div>\n</section>', start)
    cards = '\n'.join(post_card(p, '') for p in POSTS)
    body = body[:start] + '<div class="posts">\n' + cards + '\n    ' + body[end:]
    ld = jsonld({'@graph': [
      {'@type': 'WebSite', '@id': f'{SITE}/#website', 'url': SITE + '/', 'name': SITE_NAME,
       'description': f'{BOOK_TITLE}: {BOOK_SUBTITLE}, by {AUTHOR}', 'publisher': {'@id': f'{SITE}/#author'}, 'inLanguage': 'en-US'},
      {'@type': 'Book', '@id': f'{SITE}/#book', 'name': BOOK_TITLE, 'alternateName': f'{BOOK_TITLE}: {BOOK_SUBTITLE}',
       'author': {'@id': f'{SITE}/#author'}, 'isbn': BOOK_ISBN, 'bookFormat': 'https://schema.org/Paperback',
       'publisher': {'@type': 'Organization', 'name': 'Routledge'}, 'inLanguage': 'en',
       'image': f'{SITE}/images/book-cover.jpg', 'url': SITE + '/#book', 'sameAs': BOOK_URL,
       'about': ['online learning', 'blended learning', 'student engagement', 'instructional design', 'social learning', 'educational technology'],
       'description': 'A practical guide to designing online and blended courses that foster social interaction and student engagement.',
       'offers': {'@type': 'Offer', 'url': BOOK_URL, 'availability': 'https://schema.org/InStock', 'seller': {'@type': 'Organization', 'name': 'Routledge'}}},
      PERSON_LD,
    ]})
    return shell('', f'{BOOK_TITLE} · {AUTHOR} | {SITE_NAME}',
                 f'{BOOK_TITLE}: {BOOK_SUBTITLE} by {AUTHOR} (Routledge). A practical guide to designing online and blended courses that foster social interaction and student engagement.',
                 body.strip(), SITE + '/', 'book-cover.jpg', extra_head=ld,
                 og_image_alt=f'Cover of {BOOK_TITLE} by {AUTHOR}')

(ROOT / 'index.html').write_text(build_home())
(ROOT / 'blog' / 'index.html').write_text(build_blog_index())
for i, p in enumerate(POSTS):
    d = ROOT / 'blog' / p['slug']; d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(build_post(p, POSTS[1 - i]))

# a copy-and-edit template for future posts
tpl = dict(slug='your-post-slug', title='Your post title', deck='One-sentence subtitle for the post.', date='2026-01-01', date_text='January 1, 2026', read='5 min read',
           image='ai-fluency-framework.png', image_alt='Describe the image', summary='One or two sentences shown on the blog index and the home page.',
           body='''
<p>Opening paragraph.</p>
<h2>A section heading</h2>
<p>Body text. Use <a href="https://example.com">links</a>, <em>emphasis</em> and <strong>bold</strong> as usual.</p>
<div class="callouts">
  <div class="callout"><h3>A key finding</h3><p>One short paragraph.</p></div>
</div>
<figure class="fig">
  <img loading="lazy" src="../../images/your-image.png" alt="Describe the image">
  <figcaption><strong>Figure 1:</strong> caption.</figcaption>
</figure>
<blockquote class="pull">A pull quote.</blockquote>
<ol class="steps"><li><strong>Step one.</strong> Text.</li><li><strong>Step two.</strong> Text.</li></ol>
<h2>References</h2>
<ol class="refs"><li>Author, A. (2026). Title. <em>Journal</em>. <a href="https://doi.org/...">https://doi.org/...</a></li></ol>
<div class="cite"><p class="eyebrow">How to cite this post</p><p>Ou, C. (2026, January 1). <em>Your post title</em>. https://engagedigitallearning.com/blog/your-post-slug/</p></div>
''')
(ROOT / 'blog' / 'post-template.html').write_text(build_post(tpl, POSTS[0]))
# sitemap.xml and robots.txt (regenerated on every build)
import datetime
today = datetime.date.today().isoformat()
latest = max(p.get('modified', p['date']) for p in POSTS)
urls = [(SITE + '/', today, 'monthly', '1.0'), (SITE + '/blog/', today, 'monthly', '0.8')]
urls += [(f"{SITE}/blog/{p['slug']}/", p.get('modified', p['date']), 'yearly', '0.7') for p in POSTS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += ''.join(f'  <url><loc>{u}</loc><lastmod>{d}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n' for u,d,c,pr in urls)
sm += '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(sm)
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /blog/post-template.html\n\nSitemap: {SITE}/sitemap.xml\n')
print('built')
