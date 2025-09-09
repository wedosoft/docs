#!/usr/bin/env python3
"""
Translation Quality Management System for ongoing FAQ maintenance.
"""

import os
import re
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional

class TranslationQualityManager:
    """
    Manages translation quality, versioning, and validation.
    """
    
    def __init__(self, quality_db_path: str = "translation_quality.json"):
        self.quality_db_path = quality_db_path
        self.quality_db = self._load_quality_db()
    
    def _load_quality_db(self) -> Dict:
        """Load or create quality database."""
        if os.path.exists(self.quality_db_path):
            with open(self.quality_db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "files": {},
            "global_stats": {
                "total_translations": 0,
                "failed_validations": 0,
                "last_updated": None
            }
        }
    
    def _save_quality_db(self):
        """Save quality database."""
        with open(self.quality_db_path, 'w', encoding='utf-8') as f:
            json.dump(self.quality_db, f, indent=2, ensure_ascii=False)
    
    def _calculate_content_hash(self, content: str) -> str:
        """Calculate hash for content versioning."""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def record_translation(self, file_path: str, original_content: str, 
                         translated_content: str, validation_errors: Optional[List[str]] = None):
        """Record translation quality metrics."""
        content_hash = self._calculate_content_hash(original_content)
        
        file_record = {
            "file_path": file_path,
            "content_hash": content_hash,
            "translation_date": datetime.now().isoformat(),
            "original_length": len(original_content),
            "translated_length": len(translated_content),
            "validation_passed": len(validation_errors or []) == 0,
            "validation_errors": validation_errors or [],
            "quality_score": self._calculate_quality_score(original_content, translated_content, validation_errors or [])
        }
        
        self.quality_db["files"][file_path] = file_record
        self.quality_db["global_stats"]["total_translations"] += 1
        if validation_errors:
            self.quality_db["global_stats"]["failed_validations"] += 1
        self.quality_db["global_stats"]["last_updated"] = datetime.now().isoformat()
        
        self._save_quality_db()
    
    def _calculate_quality_score(self, original: str, translated: str, errors: List[str]) -> float:
        """Calculate quality score (0-100)."""
        base_score = 100.0
        
        # Deduct points for validation errors
        base_score -= len(errors) * 10
        
        # Deduct points for extreme length differences
        length_ratio = len(translated) / len(original) if len(original) > 0 else 1
        if length_ratio < 0.5 or length_ratio > 2.0:
            base_score -= 20
        
        # Deduct points for missing markdown elements
        original_md_elements = len(re.findall(r'[{}<>*_`\[\]]', original))
        translated_md_elements = len(re.findall(r'[{}<>*_`\[\]]', translated))
        if original_md_elements > 0:
            md_preservation = translated_md_elements / original_md_elements
            base_score *= md_preservation
        
        return max(0, min(100, base_score))
    
    def needs_retranslation(self, file_path: str, current_content: str) -> bool:
        """Check if file needs retranslation based on content changes."""
        if file_path not in self.quality_db["files"]:
            return True
        
        current_hash = self._calculate_content_hash(current_content)
        stored_hash = self.quality_db["files"][file_path]["content_hash"]
        
        return current_hash != stored_hash
    
    def get_quality_report(self) -> Dict:
        """Generate quality report."""
        files = self.quality_db["files"]
        if not files:
            return {"message": "No translations recorded yet"}
        
        quality_scores = [f["quality_score"] for f in files.values()]
        failed_files = [path for path, data in files.items() if not data["validation_passed"]]
        
        return {
            "total_files": len(files),
            "average_quality": sum(quality_scores) / len(quality_scores),
            "files_with_errors": len(failed_files),
            "error_rate": len(failed_files) / len(files) * 100,
            "failed_files": failed_files,
            "global_stats": self.quality_db["global_stats"]
        }
    
    def suggest_improvements(self, file_path: str) -> List[str]:
        """Suggest improvements for a specific file."""
        if file_path not in self.quality_db["files"]:
            return ["File not found in quality database"]
        
        file_data = self.quality_db["files"][file_path]
        suggestions = []
        
        if file_data["quality_score"] < 70:
            suggestions.append("Quality score is low - consider manual review")
        
        if file_data["validation_errors"]:
            suggestions.append("Fix validation errors before deployment")
        
        length_ratio = file_data["translated_length"] / file_data["original_length"]
        if length_ratio < 0.7:
            suggestions.append("Translation seems too short - check for missing content")
        elif length_ratio > 1.5:
            suggestions.append("Translation seems too long - check for redundancy")
        
        return suggestions or ["Translation quality looks good"]

## 3. Future-proof Translation Strategy

TRANSLATION_STRATEGY = """
# Long-term Translation Strategy for FAQ Documentation

## 1. Automated Pipeline Components

### Pre-translation Processing
- MDX element protection (placeholders)
- Content chunking with context preservation  
- Terminology consistency checking
- Format validation

### Translation Execution
- Google Translate API with HTML format preservation
- Rate limiting and error handling
- Batch processing with progress tracking
- Fallback mechanisms for API failures

### Post-translation Processing
- MDX element restoration
- Syntax validation
- Quality scoring
- Manual review flagging

## 2. Quality Assurance Framework

### Automated Validation
- MDX syntax checking
- Link integrity validation
- Image reference verification
- Formatting consistency

### Human Review Process
- High-risk content flagging
- Technical term accuracy
- Cultural adaptation review
- Final approval workflow

## 3. Maintenance Procedures

### Regular Updates
- Source content change detection
- Incremental translation updates
- Version control integration
- Rollback capabilities

### Monitoring & Metrics
- Translation quality scores
- Error rate tracking
- Performance monitoring
- Cost optimization

## 4. Technology Roadmap

### Short-term (1-3 months)
- Implement MDX-aware translation pipeline
- Set up quality management system
- Create validation automation
- Establish review workflows

### Medium-term (3-6 months)
- Integrate with CI/CD pipeline
- Add terminology management
- Implement A/B testing for translations
- Create performance dashboards

### Long-term (6+ months)
- Explore AI-powered quality assessment
- Consider custom translation models
- Implement real-time translation updates
- Add multi-language support automation
"""

def create_translation_config():
    """Create configuration for sustainable translation process."""
    config = {
        "translation": {
            "api_provider": "google_translate",
            "model": "nmt",
            "preserve_formatting": True,
            "target_languages": ["ko"],
            "quality_threshold": 75,
            "max_chunk_size": 4000,
            "rate_limit_delay": 0.1
        },
        "validation": {
            "mdx_syntax_check": True,
            "link_validation": True,
            "length_ratio_check": True,
            "terminology_consistency": True,
            "max_errors_allowed": 0
        },
        "quality_management": {
            "enable_scoring": True,
            "require_human_review_threshold": 70,
            "auto_retry_failed_translations": True,
            "keep_translation_history": True
        },
        "deployment": {
            "auto_deploy_threshold": 85,
            "require_approval_below_threshold": True,
            "backup_original_files": True,
            "rollback_on_build_failure": True
        }
    }
    
    return config

if __name__ == "__main__":
    # Example usage
    qm = TranslationQualityManager()
    
    # Record a sample translation
    qm.record_translation(
        "sample.md",
        "Original content with {placeholder}",
        "번역된 내용 with {placeholder}",
        []
    )
    
    # Generate report
    report = qm.get_quality_report()
    print("Quality Report:")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    # Create configuration
    config = create_translation_config()
    with open("translation_config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("\n✅ Translation strategy framework created!")
    print("📋 Next steps:")
    print("1. Test advanced translation pipeline")
    print("2. Set up quality management system")
    print("3. Integrate with build process")
    print("4. Train team on new workflow")
