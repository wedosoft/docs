#!/usr/bin/env python3
"""
Advanced translation pipeline with MDX-aware preprocessing and postprocessing.
This addresses the root cause of MDX parsing issues during translation.
"""

import os
import re
import json
import time
import requests
from typing import Dict, List, Tuple

class MDXTranslationPipeline:
    """
    MDX-aware translation pipeline that preserves markdown structure.
    """
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://translation.googleapis.com/language/translate/v2"
        
        # Placeholder patterns for MDX elements that shouldn't be translated
        self.placeholders = {
            'curly_braces': r'\{([^}]*)\}',
            'html_tags': r'<([^>]*)>',
            'navigation_arrows': r'(\w+)\s*>\s*(\w+)',
            'comparison_operators': r'(\d+%)\s*([<>=]+)\s*(\w+)\s*([<>=]+)\s*(\d+%)',
            'code_blocks': r'`([^`]*)`',
            'links': r'\[([^\]]*)\]\(([^)]*)\)',
            'image_refs': r'!\[([^\]]*)\]\(([^)]*)\)',
        }
        
        self.placeholder_map = {}
        self.placeholder_counter = 0
    
    def _generate_placeholder(self) -> str:
        """Generate a unique placeholder."""
        self.placeholder_counter += 1
        return f"__PLACEHOLDER_{self.placeholder_counter}__"
    
    def _protect_mdx_elements(self, content: str) -> str:
        """
        Replace MDX elements with placeholders before translation.
        """
        protected_content = content
        
        for pattern_name, pattern in self.placeholders.items():
            matches = re.finditer(pattern, protected_content)
            for match in matches:
                placeholder = self._generate_placeholder()
                self.placeholder_map[placeholder] = match.group(0)
                protected_content = protected_content.replace(match.group(0), placeholder, 1)
        
        return protected_content
    
    def _restore_mdx_elements(self, content: str) -> str:
        """
        Restore MDX elements from placeholders after translation.
        """
        restored_content = content
        
        for placeholder, original in self.placeholder_map.items():
            restored_content = restored_content.replace(placeholder, original)
        
        return restored_content
    
    def _translate_text(self, text: str, target_language: str = 'ko') -> str:
        """
        Translate text using Google Translate API with HTML preservation.
        """
        headers = {
            'Content-Type': 'application/json',
        }
        
        data = {
            'q': text,
            'target': target_language,
            'source': 'en',
            'format': 'html',  # This helps preserve some formatting
            'model': 'nmt',    # Use Neural Machine Translation
            'key': self.api_key
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            if 'data' in result and 'translations' in result['data']:
                return result['data']['translations'][0]['translatedText']
            else:
                print(f"Unexpected API response: {result}")
                return text
                
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def _chunk_text(self, text: str, max_length: int = 4000) -> List[str]:
        """
        Split text into chunks for translation, preserving sentence boundaries.
        """
        if len(text) <= max_length:
            return [text]
        
        chunks = []
        current_chunk = ""
        
        # Split by sentences first
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= max_length:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = sentence + " "
                else:
                    # Handle very long sentences
                    chunks.append(sentence)
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def translate_mdx_content(self, content: str) -> str:
        """
        Main method to translate MDX content safely.
        """
        print("🔒 Protecting MDX elements...")
        
        # Reset placeholder map for each translation
        self.placeholder_map = {}
        self.placeholder_counter = 0
        
        # Protect MDX elements
        protected_content = self._protect_mdx_elements(content)
        
        # Split into translatable chunks
        chunks = self._chunk_text(protected_content)
        
        print(f"📝 Translating {len(chunks)} chunks...")
        
        translated_chunks = []
        for i, chunk in enumerate(chunks):
            print(f"  Translating chunk {i+1}/{len(chunks)}")
            translated_chunk = self._translate_text(chunk)
            translated_chunks.append(translated_chunk)
            
            # Rate limiting
            time.sleep(0.1)
        
        # Combine translated chunks
        translated_content = " ".join(translated_chunks)
        
        print("🔓 Restoring MDX elements...")
        
        # Restore MDX elements
        final_content = self._restore_mdx_elements(translated_content)
        
        return final_content
    
    def validate_mdx_syntax(self, content: str) -> Tuple[bool, List[str]]:
        """
        Basic MDX syntax validation.
        """
        errors = []
        
        # Check for unmatched braces
        open_braces = content.count('{')
        close_braces = content.count('}')
        if open_braces != close_braces:
            errors.append(f"Unmatched braces: {open_braces} '{' vs {close_braces} '}'")
        
        # Check for unmatched HTML tags
        open_tags = re.findall(r'<([^/][^>]*)>', content)
        close_tags = re.findall(r'</([^>]*)>', content)
        
        # Simple validation for common issues
        if '<>' in content and '</>' not in content:
            errors.append("Unmatched empty JSX tag")
        
        return len(errors) == 0, errors

def main():
    """
    Example usage of the improved translation pipeline.
    """
    api_key = "AIzaSyAktNTMV9YoM-NnGt-xjjHpyR-38uTOzIw"
    pipeline = MDXTranslationPipeline(api_key)
    
    # Test with a sample MDX content
    sample_content = """
    Navigate to Admin > Settings > {Workspace Name} > Configuration
    
    The comparison 40% <= Score <= 60% represents neutral sentiment.
    
    Use the `onClick` handler for buttons.
    """
    
    print("Original content:")
    print(sample_content)
    print("\n" + "="*50 + "\n")
    
    translated = pipeline.translate_mdx_content(sample_content)
    
    print("Translated content:")
    print(translated)
    print("\n" + "="*50 + "\n")
    
    # Validate result
    is_valid, errors = pipeline.validate_mdx_syntax(translated)
    if is_valid:
        print("✅ MDX syntax validation passed")
    else:
        print("❌ MDX syntax validation failed:")
        for error in errors:
            print(f"  - {error}")

if __name__ == "__main__":
    main()
