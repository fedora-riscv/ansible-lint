%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        3.1.2
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
%{__python2} setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_lint-%{version}-py2.*.egg-info

%changelog
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

