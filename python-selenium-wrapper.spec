Name:		python-selenium-wrapper
Version:	0.1
Release:	1%{?dist}
Summary:	Selenium driver wrapper and nosetests screenhots plugin

Group:		Development/Tools
License:	GPLv3+
URL:		https://github.com/RedHatQE/python-selenium-wrapper
Source0:	%{name}-%{version}.tar.gz
BuildArch:  	noarch

BuildRequires:	python-devel
Requires:	python-nose

%description
%{summary}

%prep
%setup -q

%build

%install
%{__python} setup.py install -O1 --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/python-selenium-wrapper/*.py*
%{python_sitelib}/python-selenium-wrapper/nose/*.py*

%changelog
* Fri July 12 2013 dparalen 0.1-1
- new package built with tito

