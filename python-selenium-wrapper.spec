Name:		python-selenium-wrapper
Version:	0.9
Release:	1%{?dist}
Summary:	Selenium driver wrapper and nosetests screenhots plugin

Group:		Development/Tools
License:	GPLv3+
URL:		https://github.com/RedHatQE/python-selenium-wrapper
Source0:	%{name}-%{version}.tar.gz
BuildArch:  	noarch

BuildRequires:	python-devel
Requires:	python-nose, python-selenium

%description
%{summary}

%prep
%setup -q

%build

%install
%{__python} setup.py install --single-version-externally-managed -O1 --root $RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/selenium_wrapper/*.py*
%{python_sitelib}/selenium_wrapper/nose/*.py*

%changelog
* Tue Mar 04 2014 dparalen <vetrisko@gmail.com> 0.9-1
- fix: missing provides (vetrisko@gmail.com)

* Mon Aug 26 2013 dparalen <vetrisko@gmail.com> 0.8-1
- introducing test cases for current_url context manager (vetrisko@gmail.com)
- fix: try---finally (vetrisko@gmail.com)
- fix import (vetrisko@gmail.com)
- fix import (vetrisko@gmail.com)
- introducing some driver handling (vetrisko@gmail.com)

* Fri Aug 23 2013 dparalen <vetrisko@gmail.com> 0.7-1
- clean up: tests (vetrisko@gmail.com)
- fix: catch possible os errors in formating failures (vetrisko@gmail.com)

* Fri Aug 16 2013 dparalen <vetrisko@gmail.com> 0.6-1
- fix: quit instead of close cleans temporary firefox profile
  (vetrisko@gmail.com)
- implementing a retry logic creating snapshots (vetrisko@gmail.com)

* Thu Aug 15 2013 dparalen <vetrisko@gmail.com> 0.5-1
- introducing helper context managers for navigating: current_url, restore_url
  (vetrisko@gmail.com)

* Thu Aug 08 2013 dparalen <vetrisko@gmail.com> 0.4-1
- fix: import error (vetrisko@gmail.com)

* Thu Aug 08 2013 dparalen <vetrisko@gmail.com> 0.3-1
- fix: warn when unable to take screenshots (vetrisko@gmail.com)
- fix: dependencies (vetrisko@gmail.com)
- fix: installation (vetrisko@gmail.com)
- fix: required to be a staticmethod (vetrisko@gmail.com)
- introducing a simple test case (vetrisko@gmail.com)
- Update README.md (vetrisko@gmail.com)
- introducing short description of the webui screenshots plugin
  (vetrisko@gmail.com)
- fix: paths (vetrisko@gmail.com)

* Fri Jul 12 2013 dparalen <vetrisko@gmail.com> 0.2-1
- new package built with tito


