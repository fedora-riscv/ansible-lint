%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        2.3.3
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

License:        MIT
URL:            https://github.com/willthames/ansible-lint
Source0:        https://pypi.python.org/packages/source/a/%{archive_name}/%{archive_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  ansible
Requires:       ansible

%description
Checks playbooks for practices and behavior that could potentially be improved

%prep
%setup -q -n %{archive_name}-%{version}
rm -rf *.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root=%{buildroot}

%check
%{__python2} setup.py test

%files
%doc PKG-INFO 
%license LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_lint-%{version}-py2.*.egg-info

%changelog
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

