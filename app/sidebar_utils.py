import base64
from pathlib import Path
import streamlit as st

def add_sidebar_author():
    assets_dir = Path(__file__).resolve().parent / "assets"
    dest_img = assets_dir / "author_image.jpg"
    img_base64 = ""
    if dest_img.exists():
        try:
            with open(dest_img, "rb") as f:
                img_base64 = base64.b64encode(f.read()).decode("utf-8")
        except Exception:
            pass

    avatar_html = (
        f'<img src="data:image/jpeg;base64,{img_base64}" class="sidebar-author-img" />'
        if img_base64
        else '<div class="sidebar-author-avatar-text">MA</div>'
    )

    sidebar_html = f"""
    <div class="sidebar-author-card">
        <div class="sidebar-author-header">
            <div class="sidebar-author-avatar-container">
                {avatar_html}
            </div>
            <div class="sidebar-author-info">
                <div class="sidebar-author-name">Mohamed Abbas</div>
            </div>
        </div>
        <div class="sidebar-author-title">Data Scientist & ML Engineer</div>
        <div class="sidebar-author-details">
            <p>📍 Cairo, Egypt</p>
            <p>📧 <a href="mailto:m.abbaas22@gmail.com" class="sidebar-detail-link">m.abbaas22@gmail.com</a></p>
            <p>📞 <a href="tel:+201010262040" class="sidebar-detail-link">+20 101 026 2040</a></p>
        </div>
        <div class="sidebar-author-socials">
            <a href="https://www.linkedin.com/in/m-abbas-el-sharif/" target="_blank" class="sidebar-social-btn linkedin" title="LinkedIn">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
            </a>
            <a href="https://github.com/M-Abbas-El-Sharif" target="_blank" class="sidebar-social-btn github" title="GitHub">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://wa.me/201010262040" target="_blank" class="sidebar-social-btn whatsapp" title="WhatsApp">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.513 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.734-1.455L0 24zm6.59-4.846c1.6.95 3.188 1.449 4.625 1.45 5.489 0 9.953-4.467 9.957-9.96.002-2.661-1.034-5.166-2.918-7.05C16.427 1.709 13.927.673 11.997.673 6.511.673 2.046 5.14 2.043 10.63c-.001 1.513.437 3.006 1.268 4.298L2.247 21.03l6.398-1.677-.001-.001zM17.472 14.382c-.3-.149-1.777-.878-2.046-.977-.269-.099-.465-.149-.661.15-.196.299-.759.957-.93 1.15-.171.199-.343.224-.643.075-.3-.15-1.267-.467-2.413-1.488-.891-.796-1.493-1.779-1.668-2.079-.175-.299-.019-.462.13-.611.135-.134.3-.349.45-.524.15-.174.199-.299.299-.499.1-.2.05-.375-.025-.524-.075-.15-.661-1.597-.905-2.184-.239-.575-.483-.497-.661-.506-.171-.009-.368-.01-.565-.01-.197 0-.517.074-.787.374-.269.299-1.029 1.002-1.029 2.443 0 1.441 1.049 2.831 1.196 3.031.147.2 2.062 3.149 4.996 4.417.697.302 1.242.482 1.666.617.7.223 1.338.192 1.843.117.563-.083 1.777-.726 2.027-1.429.25-.702.25-1.304.175-1.43-.075-.125-.269-.199-.569-.349z"/>
                </svg>
            </a>
            <a href="https://m-abbas-el-sharif.github.io/" target="_blank" class="sidebar-social-btn portfolio" title="Portfolio">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                </svg>
            </a>
        </div>
    </div>
    """
    st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)
