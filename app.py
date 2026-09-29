from flask import Flask, render_template, abort

app = Flask(__name__)

posts = [
    {
        "slug": "life",
        "title": "Life is not hard or harmful",
        "subtitle": "That’s exactly what they taught and showed us",
        "date": "Jan 15, 2026",
        "topic": "Thought",
        "image": "https://framerusercontent.com/images/fnHX6gCXCG7Pkrrfa5vw1u00vs.jpg?width=736&height=642",
        "featured": True,
        "content": [
            "Life is not hard or harmful. That’s exactly what they taught and showed us.",
            "Why can’t we love and enjoy what we do worse than others? Why do we begin to hate someone who performs better than us?",
            "Because we still haven’t accepted our own identity.",
            "Why do we conceal our mistakes—not only religious ones, but also the mistakes essential for our growth?",
            "Because we fear their opinions and their laughter. Yet that laughter doesn’t affect us in the slightest.",
            "Where did we go wrong?",
            "They taught us to become the best according to their vision, to strive for what they wanted us to be. And that made our life even heavier.",
            "We forgot to become the best version of ourselves.",
            "There is no need to illustrate these truths with examples. Because these are pains spoken from myself to myself, from yourself to yourself."
        ],
        "source": "https://lb.framer.wiki/all-posts/life"
    },
    {
        "slug": "mental-models",
        "title": "How to Truly Remember What You Read",
        "subtitle": "It’s not about memorizing — it’s about building mental models",
        "date": "Feb 4, 2026",
        "topic": "Psychology",
        "image": None,
        "featured": True,
        "content": [
            "Most of us highlight important parts, write notes in the margins, and sometimes copy whole pages or paragraphs.",
            "The result? A few weeks later, almost nothing remains from that book in our memory.",
            "The core problem is passive reading and surface-level notes.",
            "Reading should not be about collecting information. It should be about understanding relationships between ideas.",
            "A useful mental model connects new knowledge to what you already understand.",
            "Notes should be kept to an absolute minimum. The best note is the one you never had to write.",
            "If you do write notes, use your own words, keep them short, and turn them into questions for your future self.",
            "Before deep reading, skim the table of contents, look at the chapter titles and read the introduction and conclusion.",
            "The goal of reading is not to finish more books. The goal is to continuously upgrade the way you see the world, the way you think, and the way you approach problems.",
            "Real knowledge is a living, growing, densely connected web inside your mind."
        ],
        "source": "https://lb.framer.wiki/all-posts/mental-models"
    },
    {
        "slug": "about-me",
        "title": "Do you know about me!?",
        "subtitle": "Sure, you know a bit about me—but do you really?",
        "date": "Jan 14, 2026",
        "topic": "Myself",
        "image": "https://framerusercontent.com/images/ARxoaw4nlU1IDdN0JT7sb7QMhc.jpg?width=900&height=506",
        "featured": True,
        "content": [
            "You know!",
            "Read these blog posts—my thoughts and my perspective—and discover me.",
            "I believe people are revealed through the things they notice, the questions they ask, and the way they explain what they learn.",
            "This blog is a small archive of those thoughts."
        ],
        "source": "https://lb.framer.wiki/all-posts/about-me"
    },
    {
        "slug": "anjuman",
        "title": "The forum that completely changed me | Part 1",
        "subtitle": "Memories, friendship & atmosphere",
        "date": "Feb 6, 2026",
        "topic": "Life",
        "image": None,
        "featured": False,
        "content": [
            "This was my first time going to a forum.",
            "At this forum, organized by the Children's Organization, our school received an offer in the startup direction. Based on a selection, I decided to participate.",
            "I was on vacation when the deputy director of our school contacted me and told me to take part in the forum.",
            "At first, I didn’t like the idea because I felt uncomfortable among many people. But I decided to take a risk.",
            "I arrived at the station, and our team also arrived. Although I didn’t know them well, they tried to talk to me and get to know me.",
            "We boarded the train and set off. The joy in their eyes evoked a peculiar feeling in me.",
            "When we arrived, representatives from each city showcased the traditions of their nation.",
            "My main purpose in coming was to improve my communication skills and discover new things.",
            "More in the next post."
        ],
        "source": "https://lb.framer.wiki/all-posts/anjuman"
    }
]


@app.route("/")
def home():
    featured_posts = [post for post in posts if post["featured"]]
    return render_template(
        "index.html",
        posts=posts,
        featured_posts=featured_posts
    )


@app.route("/all-posts")
def all_posts():
    return render_template(
        "index.html",
        posts=posts,
        featured_posts=posts
    )


@app.route("/post/<slug>")
def post_detail(slug):
    post = next((post for post in posts if post["slug"] == slug), None)

    if not post:
        abort(404)

    current_index = posts.index(post)
    previous_post = posts[current_index - 1] if current_index > 0 else None
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None

    return render_template(
        "post.html",
        post=post,
        previous_post=previous_post,
        next_post=next_post
    )


@app.route("/contact")
def contact():
    return render_template("index.html", posts=[], featured_posts=[])


if __name__ == "__main__":
    app.run(debug=True)
