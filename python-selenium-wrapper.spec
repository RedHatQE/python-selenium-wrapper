Name:		python-selenium-wrapper
Version:	0.3
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


