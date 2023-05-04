interface RssLink {
  title: string
  slug: string
}

interface RssEntry {
  title: string
  link: string
  published: string
}

interface RssFeed {
  entries: RssEntry[]
}
