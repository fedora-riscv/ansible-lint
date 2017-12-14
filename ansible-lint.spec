%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        3.4.19
Release:        3%{?dist}
Summary:        Best practices checker for Ansible

License:        MIT
URL:            https://github.com/willthames/ansible-lint
Source0:        https://github.com/willthames/%{archive_name}/archive/v%{version}.tar.gz

BuildArch:      noarch

%global _description\
Checks playbooks for practices and behavior that could potentially be improved\

%description %_description

%package -n python2-%{archive_name}
Summary:        %summary
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  ansible
Requires:       ansible
%{?python_provide:%python_provide python2-%{archive_name}}
Provides:       %{archive_name} = %{version}-%{release}
Obsoletes:      %{archive_name} < 3.4.19-2

%description  -n python2-%{archive_name} %_description

%package -n python3-%{archive_name}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  ansible-python3
Requires:       ansible-python3
%{?python_provide:%python_provide python3-%{archive_name}}

%description  -n python3-%{archive_name} %_description

%prep
%autosetup -n %{archive_name}-%{version}

%build
%py2_build
%py3_build

%install
%py3_install
# Rename Python 3 executable file
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3

%py2_install

%check
# Following sed execution is necessary for test/TestCommandLineInvocationSameAsConfig.py
sed -i 's|/usr/bin/env python|%{_bindir}/python2|' bin/ansible-lint
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} setup.py test
sed -i 's|%{_bindir}/python2|%{_bindir}/python3|' bin/ansible-lint
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python2-%{archive_name}
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_lint-%{version}-py2.*.egg-info

%files -n python3-%{archive_name}
%doc README.md
%license LICENSE
%{_bindir}/%{name}-3
%{python3_sitelib}/%{lib_name}
%{python3_sitelib}/ansible_lint-%{version}-py3.*.egg-info

%changelog
* Thu Dec 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.19-3
- Fix the test/TestCommandLineInvocationSameAsConfig.py execution for python3

* Wed Dec 13 2017 Jan Beran <jberan@redhat.com> - 3.4.19-2
- Python 2 binary package renamed to python2-ansible-lint
- Python 3 subpackage

* Mon Dec 11 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.19-1
- Update to 3.4.19 version (#1524156)

* Sun Oct 22 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.17-1
- Update to 3.4.17 version (#1505124)

* Tue Oct 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.16-1
- Update to 3.4.16 version (#1497872)

* Sat Sep 02 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.15-1
- Update to 3.4.15 version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.13-1
- Update to 3.4.13 version

* Mon Mar 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.12-1
- Update to 3.4.12 version

* Mon Feb 13 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.11-1
- Update to 3.4.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.10-1
- Update to 3.4.10

* Thu Dec 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.9-1
- Update to 3.4.9

* Fri Dec 16 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.8-1
- Update to 3.4.8

* Mon Dec 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.7-1
- Update to 3.4.7

* Tue Nov 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.4-1
- Update to 3.4.4

* Tue Nov 08 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.3-1
- Update to 3.4.3

* Fri Oct 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.1-1
- Update to 3.4.1

* Fri Sep 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.3-1
- Update to 3.3.3

* Fri Sep 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.2-1
- Update to 3.3.2

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.5-1
- Update to 3.2.5

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.4-1
- Update to 3.2.4

* Wed Jul 27 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.1-1
- Upstream release 3.2.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 18 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.0-1
- Upstream release 3.2.0

* Fri Jul 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.3-1
- Upstream release 3.1.3

* Thu Jul 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.2-1
- Upstream release 3.1.2

* Thu Jun 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.1-1
- Upstream release 3.1.1

* Wed Jun 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.0-1
- Upstream release 3.1.0

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-2
- Fixed typo in previous changelog entry

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-1
- Update to 3.0.1 release

* Thu Jun 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0 release

* Tue May 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.6.2-1
- Update to 2.6.2 release

* Sat Mar 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.4.1-1
- Update to 2.4.1 release

* Wed Mar 16 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.4.0-1
- Update to 2.4.0 release

* Thu Mar 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.9-1
- Update to 2.3.9 release

* Fri Feb 26 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.8-1
- Update to 2.3.8 release

* Sat Feb 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.5-1
- Update to 2.3.5 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.3-1
- Update to 2.3.3 release

* Fri Jan 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.1-1
- Update to 2.3.1 release

* Fri Jan 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0 release

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Update to 2.2.0

* Tue Nov 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-1
- Update to 2.1.0

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.3-1
- Update to 2.0.3

* Fri Dec 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- Update to 2.0.1

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- rename to ansible-lint
- new upstream 1.0.4 release which added LICENSE file.

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- Better add upstream LICENSE file, not present in tarball

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

