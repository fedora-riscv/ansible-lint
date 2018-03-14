%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        3.4.21
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

License:        MIT
URL:            https://github.com/willthames/ansible-lint
Source0:        https://github.com/willthames/%{archive_name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  ansible
Requires:       ansible

%description
Checks playbooks for practices and behavior that could potentially be improved

%prep
%autosetup -n %{archive_name}-%{version}
rm -rf *.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%py2_build

%install
%py2_install

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_lint-%{version}-py2.*.egg-info

%changelog
* Wed Mar 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.21-1
- Update to 3.4.21 version (#1555095)

* Mon Dec 11 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.19-1
- Update to 3.4.19 version (#1524156)

* Sun Oct 22 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.17-1
- Update to 3.4.17 version (#1505124)

* Sat Sep 02 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.15-1
- Update to 3.4.15 version

* Wed May 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.13-1
- Update to 3.4.13 version

* Mon Mar 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.12-1
- Update to 3.4.12 version

* Mon Feb 13 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.11-1
- Update to 3.4.11

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

* Fri Jul 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.3-1
- Upstream release 3.1.3

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-2
- Fixed typo in previous changelog entry

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-1
- Update to 3.0.1 release

* Thu Jun 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0 release

* Sat May 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.6.2-1
- Update to 2.6.2
- use %license macro
- disable tests

* Fri Dec 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- Update to 2.0.1

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- rename to ansible-lint
- new upstream 1.0.4 release which added LICENSE file.

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- Better add upstream LICENSE file, not present in tarball

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

