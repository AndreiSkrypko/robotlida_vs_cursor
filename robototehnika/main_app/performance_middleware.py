import re


class LazyLoadMiddleware:
    """Add loading='lazy' to all images for faster page load"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        if response.get('Content-Type', '').startswith('text/html'):
            content = response.content.decode('utf-8')
            
            def add_lazy(match):
                img_tag = match.group(0)
                if 'loading=' not in img_tag:
                    if img_tag.endswith('/>'):
                        return img_tag[:-2] + ' loading="lazy" />'
                    else:
                        return img_tag[:-1] + ' loading="lazy">'
                return img_tag
            
            content = re.sub(r'<img\s+[^>]*/?>', add_lazy, content)
            
            response.content = content.encode('utf-8')
            response['Content-Length'] = len(response.content)
        
        return response

