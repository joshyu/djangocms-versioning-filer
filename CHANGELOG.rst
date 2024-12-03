=========
Changelog
=========

Unreleased
==========
* make it compatible with django-filer 3.3+
* make it compatible with CMS 4.1+

1.3.2 (2024-11-12)
==========
* fixed compatibility with djangocms-versioning 2
  
1.3.1 (2024-09-19)
==========
* list per page added to folderadmin to read from request parameters

1.3.0 (2024-05-16)
==========
* Django 4.2 support added
* Django 2.2 support removed
* Python 3.10 support added
* Python 3.7 support removed

1.2.3 (2024-03-05)
==========
* fix: delete published thumbnail image when publishing/unpublishing images.
  
1.2.2 (2023-08-09)
==========
* fix: Filer admin to point correct change form template

1.2.1 (2022-11-14)
==================
* fix: Add missing closing quotation in template

1.2.0 (2022-11-01)
==================
* feat: Added edit icon to file changelist

1.1.0 (2022-10-14)
==========
* feat: Enable sorting by headers on the monkey patched directory_listing admin view
* feat: Replace CircleCi with GitHub Actions for linting and tests
* fix: File download burger menu link does not open in a new tab as per previous behavior
* feat: Customisable folder list admin file action buttons

1.0.0 (2022-04-25)
==================
* feat: Added file list item actions burger menu
* fix: Missing icon images in latest filer 2.x where the icons are now SVG
* Python 3.8, 3.9 support added
* Django 3.0, 3.1 and 3.2 support added
* Python 3.5 and 3.6 support removed
* Django 1.11 support removed
