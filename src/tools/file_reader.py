from langchain_core.tools import tool

@tool
def read_file(file_path: str) -> str:
    """读取文件内容（支持 .txt, .pdf, .docx）
    当用户需要读取简历文件内容时调用该工具，必须传入完整文件路径。
    Args:
        file_path: 文件路径
    """
    try:
        if file_path.endswith('.pdf'):
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            content = '\n'.join([page.extract_text() for page in reader.pages if page.extract_text()])
            return content
        elif file_path.endswith('.docx'):
            from docx import Document
            doc = Document(file_path)
            content = '\n'.join([para.text for para in doc.paragraphs])
            return content
        else:
            # 默认按文本文件读取
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    except FileNotFoundError:
        return f"文件不存在：{file_path}"
    except Exception as e:
        return f"读取失败：{str(e)}"


