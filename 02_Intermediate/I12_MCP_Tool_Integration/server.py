from mcp.server.fastmcp import FastMCP
server=FastMCP('learning-word-counter')
@server.tool()
def count_words(text:str)->int:
    """Count words in at most 2000 characters. No filesystem or network access."""
    if not text.strip() or len(text)>2000: raise ValueError('Enter 1–2000 characters.')
    return len(text.split())
if __name__=='__main__':server.run(transport='stdio')
